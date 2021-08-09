from infraestructure.repository.agent import WitRepository
from domain.agent.channels import WebChannel, BaseChannel
from domain.models.agent import RequestModel, CommandModel
from domain.agent.commands import GreetingCommand, BaseCommand, OrdersReportCommand


class AgentService:
    def __init__(self, userId: int):
        self.nlp = WitRepository()
        self.userId = userId

    def init_web_conversation(self, request: RequestModel):
        channel = WebChannel(self.userId)
        command = CommandModel(**self.nlp.get_command(request.message))
        print(command)
        chain = self.__build_chain(channel, command)
        return chain.next()

    def __build_chain(self, channel: BaseChannel, command: CommandModel) -> BaseCommand:
        orders_report_command = OrdersReportCommand(channel, command, None)
        greeting_command = GreetingCommand(
            channel, command, successor=orders_report_command)
        return greeting_command
