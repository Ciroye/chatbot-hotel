from domain.agent.commands.base_command import BaseCommand
from domain.models.agent import ResponseModel
from infraestructure.repository.agent import AgentRepository


class GreetingCommand(BaseCommand):
    def __init__(self, channel, command, successor=None):
        super().__init__(channel, command, successor=successor, command_intent='greeting')
        self.requirements = []
        self.repository = AgentRepository()

    def next(self):
        if self.is_command():
            if self.meet_requirements():
                return self.send(ResponseModel(message="Hi there buddy!"))
            else:
                return self.ask_for_requirements()

        if self.successor is not None:
            return self.successor.next()
