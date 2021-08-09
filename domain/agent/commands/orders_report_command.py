from domain.agent.commands.base_command import BaseCommand
from domain.models.agent import RequirementModel


class OrdersReportCommand(BaseCommand):
    def __init__(self, channel, command, successor=None):
        super().__init__(channel, command, successor=successor, command_intent='request_report')
        self.requirements = [
            RequirementModel(requireEntity="divisions", questions=["De qué división quieres el informe?", "Y qué divisón te interesa?"])
        ]

    def next(self):
        if self.is_command():
            if self.meet_requirements():

                print(self.command.entities)
                for e in self.command.entities:
                    return self.send({"message": f"hello {e.value} !"})

            else:
                return self.ask_for_requirements()

        if self.successor is not None:
            return self.successor.next()
