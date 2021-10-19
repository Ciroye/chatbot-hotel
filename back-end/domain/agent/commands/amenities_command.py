import datetime
import random

from domain.agent.commands.base_command import BaseCommand
from domain.models.agent import RequirementModel, ResponseModel
from domain.models.db.Reserves import Reserve
from domain.models.db.room import Room
from infraestructure.repository.agent import AgentRepository


class AmenitiesCommand(BaseCommand):
    def __init__(self, channel, command, successor=None):
        super().__init__(channel, command, successor=successor, command_intent='ask_for_amenities')
        self.repository = AgentRepository()
        self.requirements = [
            RequirementModel(requireEntity="room", questions=["Which room?"]),
        ]

    def next(self):
        if self.is_command():
            if self.meet_requirements():
                try:
                    room = self.__string_to_int__(self.get_entity('room').value)
                    rooms = [Room(**r) for r in self.repository.get_rooms() if r['code'] == room]
                    if len(rooms) > 0:
                        amenities = ", ".join(rooms[0].amenities)
                        return self.send(ResponseModel(message="The amenities for this room are: " + amenities))
                    else:
                        return self.send(ResponseModel(message="Room dot found!"))
                except Exception as ex:
                    self.__reset_context__()
                    return self.send(ResponseModel(message="Sorry"))
            else:
                return self.ask_for_requirements()
        if self.successor is not None:
            return self.successor.next()

    @staticmethod
    def __build_response__(room: str, start_date: datetime, end_date: datetime, quantity, duration):
        return f"Your assigned room is: {room} " \
               f"Since: {start_date.strftime('%d-%m-%Y')}" \
               f"Until: {end_date.strftime('%d-%m-%Y')}" \
               f"For {duration} days and {quantity} people"

    @staticmethod
    def __string_to_int__(value):
        numbers = [int(s) for s in value.split() if s.isdigit()]
        return numbers[0] if len(numbers) > 0 else 0
