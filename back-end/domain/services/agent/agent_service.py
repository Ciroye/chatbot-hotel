from domain.agent.channels import WebChannel, BaseChannel
from domain.agent.commands import GreetingCommand, BaseCommand
from domain.agent.commands.reserve_room import ReserveRoomCommand
from domain.models.agent import RequestModel, CommandModel
from infraestructure.repository.agent import WitRepository


class AgentService:
    def __init__(self):
        self.nlp = WitRepository()

    def init_web_conversation(self, request: RequestModel):
        channel = WebChannel()
        command = CommandModel(**self.nlp.get_command(request.message))
        chain = self.__build_chain__(channel, command)
        return chain.next()

    @staticmethod
    def __build_chain__(channel: BaseChannel, command: CommandModel) -> BaseCommand:
        orders_report_command = ReserveRoomCommand(channel, command, None)
        greeting_command = GreetingCommand(channel, command, successor=orders_report_command)
        return greeting_command
