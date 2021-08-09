from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import List

from domain.agent.channels import BaseChannel
from domain.models.agent import CommandModel, ResponseModel, RequirementModel


class BaseCommand(metaclass=ABCMeta):
    def __init__(self, channel: BaseChannel, command: CommandModel, successor: BaseCommand = None, command_intent: str = None):
        self.channel = channel
        self.successor = successor
        self.command = command
        self.command_intent = command_intent
        self.requirements: List[RequirementModel] = []
        self.cacheEntities = []

    @abstractmethod
    def next(self) -> ResponseModel:
        pass

    def is_command(self) -> bool:
        return self.command_intent in self.command.intents

    def meet_requirements(self) -> bool:
        entities = [e.name for e in self.command.entities if e.name and e.value]
        for r in self.requirements:
            if r.requireEntity not in entities:
                return False
        return True

    def ask_for_requirements(self) -> ResponseModel:
        """
        entities = [e.name for e in self.command.entities if e.name and e.value]
        for r in self.requirements:
            if r.requireEntity not in entities:
                self.channel.set_user_context(self.command_intent)
                self.channel.set_command_context(r.requireEntity)
                if len(self.cacheEntities) <= 0:
                    self.channel.set_user_context_value(
                        [e.dict() for e in self.command.entities])
                else:
                    self.channel.set_user_context_value(self.cacheEntities)
                option = random.randint(0, len(r.questions) - 1)
                return ResponseModel(message=r.questions[option])
        :return:
        """
        return ResponseModel()

    @staticmethod
    def send(response: ResponseModel) -> ResponseModel:
        return response
