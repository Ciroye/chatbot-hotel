import datetime
import random

from domain.agent.commands.base_command import BaseCommand
from domain.models.agent import RequirementModel, ResponseModel
from domain.models.db.Reserves import Reserve
from domain.models.db.room import Room
from infraestructure.repository.agent import AgentRepository


class CheckForReserveCommand(BaseCommand):
    def __init__(self, channel, command, successor=None):
        super().__init__(channel, command, successor=successor, command_intent='ask_for_reservation')
        self.repository = AgentRepository()
        self.requirements = [
            RequirementModel(requireEntity="room", questions=["Which room?"]),
        ]

    def next(self):
        if self.is_command():
            if self.meet_requirements():
                try:
                    room = self.__string_to_int__(self.get_entity('room').value)
                    reserves = [Reserve(**r) for r in self.repository.get_reserves() if r['code'] == room]
                    return self.send(ResponseModel(message="\n".join([self.__build_response__(r) for r in reserves])))
                except Exception as ex:
                    self.__reset_context__()
                    return self.send(ResponseModel(message="Sorry"))
            else:
                return self.ask_for_requirements()
        if self.successor is not None:
            return self.successor.next()

    @staticmethod
    def __build_response__(room: Reserve):
        return f"The room {room.code} has these reservations: " \
               f"Since: {room.start.strftime('%d-%m-%Y')}" \
               f"Until: {room.end.strftime('%d-%m-%Y')}"

    @staticmethod
    def __string_to_int__(value):
        numbers = [int(s) for s in value.split() if s.isdigit()]
        return numbers[0] if len(numbers) > 0 else 0
