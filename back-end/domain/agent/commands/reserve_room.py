import datetime
import random

from domain.agent.commands.base_command import BaseCommand
from domain.models.agent import RequirementModel, ResponseModel
from domain.models.db.Reserves import Reserve
from domain.models.db.room import Room
from infraestructure.repository.agent import AgentRepository


class ReserveRoomCommand(BaseCommand):
    def __init__(self, channel, command, successor=None):
        super().__init__(channel, command, successor=successor, command_intent='reserve_hotel')
        self.repository = AgentRepository()
        self.requirements = [
            RequirementModel(requireEntity="quantity", questions=["How many people do you want to reserve?",
                                                                  "Is it just for you? or are you going to be with someone else?"]),
            RequirementModel(requireEntity="start_date", questions=["What date do you want to do the check in? (dd-mm-yyyy)"]),
            RequirementModel(requireEntity="duration", questions=["How long you expect to stay?"])
        ]

    def next(self):
        if self.is_command():
            if self.meet_requirements():
                rooms = [Room(**r) for r in self.repository.get_rooms()]
                available_rooms = [r for r in rooms if r.capacity == int(self.get_entity('quantity').value)]
                reserves = [Reserve(**r) for r in self.repository.get_reserves()]

                start_date = datetime.datetime.strptime(self.get_entity('start_date').value, '%d-%m-%Y')
                end_date = start_date + datetime.timedelta(days=int(self.get_entity('duration').value))
                final_rooms = []
                for r in available_rooms:
                    reserve = next((rs for rs in reserves if rs.code == r.code), None)
                    if reserve is not None:
                        if not (reserve.start.replace(tzinfo=None) <= end_date <= reserve.end.replace(tzinfo=None)) and not (
                                reserve.start.replace(tzinfo=None) <= start_date <= reserve.end.replace(tzinfo=None)):
                            final_rooms.append(r)
                    else:
                        final_rooms.append(r)
                return self.send(ResponseModel(message=random.choice(final_rooms).code if len(final_rooms) > 0 else "There's no available rooms"))
            else:
                return self.ask_for_requirements()
        if self.successor is not None:
            return self.successor.next()
