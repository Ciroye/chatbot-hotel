from domain.agent.commands.base_command import BaseCommand
from domain.models.agent import ResponseModel
from infraestructure.repository.agent import AgentRepository


class FallbackCommand(BaseCommand):
    def __init__(self, channel, command, successor=None):
        super().__init__(channel, command, successor=successor, command_intent='greeting')
        self.requirements = []
        self.repository = AgentRepository()

    def next(self):
        return self.send(ResponseModel(message="Sorry, i cant understand :("))

