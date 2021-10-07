from domain.agent.channels import WebChannel, BaseChannel
from domain.agent.commands import GreetingCommand, BaseCommand
from domain.agent.commands.amenities_command import AmenitiesCommand
from domain.agent.commands.check_for_reserve_command import CheckForReserveCommand
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
        reserve_command = ReserveRoomCommand(channel, command, None)
        check_reserve_command = CheckForReserveCommand(channel, command, successor=reserve_command)
        amenities_command = AmenitiesCommand(channel, command, successor=check_reserve_command)
        greeting_command = GreetingCommand(channel, command, successor=amenities_command)
        return greeting_command
