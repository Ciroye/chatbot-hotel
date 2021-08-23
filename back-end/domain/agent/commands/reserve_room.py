from domain.agent.commands.base_command import BaseCommand
from domain.models.agent import RequirementModel


class ReserveRoomCommand(BaseCommand):
    def __init__(self, channel, command, successor=None):
        super().__init__(channel, command, successor=successor, command_intent='reserve_hotel')
        self.requirements = [
            RequirementModel(requireEntity="quantity", questions=["How many people do you want to reserve?",
                                                                  "Is it just for you? or are you going to be with someone else?"]),
        ]

    def next(self):
        if self.is_command():
            if self.meet_requirements():
                print("--------Logic goes here-----------")
                print(self.command.json())
                return self.send({"message": f"hello Mf !"})
            else:
                return self.ask_for_requirements()
        if self.successor is not None:
            return self.successor.next()
