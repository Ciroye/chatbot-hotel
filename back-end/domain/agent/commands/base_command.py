from __future__ import annotations

import random
from abc import ABCMeta, abstractmethod
from typing import List, Optional

from domain.agent.channels import BaseChannel
from domain.models.agent import CommandModel, ResponseModel, RequirementModel, CommandEntity


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
        return self.command_intent in self.command.intents or self.__is_context_action__()

    def meet_requirements(self) -> bool:
        if self.__is_context_action__():
            self.cacheEntities = self.__fill_entities__()
        entities = [e.name for e in self.command.entities if e.name and e.value]
        for r in self.requirements:
            if r.requireEntity not in entities:
                return False
        return True

    def __is_context_action__(self):
        return self.command_intent == self.channel.context

    def __fill_entities__(self):
        self.__check_command_step__()
        entities = self.channel.cache.get_user_context_value()
        if entities:
            for e in entities:
                self.command.entities.append(CommandEntity(**e))
            return entities
        return []

    def __check_command_step__(self):
        command_step = self.channel.cache.get_command_context()
        if command_step:
            entities = self.channel.cache.get_user_context_value()
            if entities:
                entities.append({"name": command_step, "value": self.command.text})
            else:
                entities = [{"name": command_step, "value": self.command.text}]
            self.channel.cache.set_user_context_value(entities)

    def ask_for_requirements(self) -> ResponseModel:
        entities = [e.name for e in self.command.entities if e.name and e.value]
        for r in self.requirements:
            if r.requireEntity not in entities:
                self.channel.cache.set_user_context(self.command_intent)
                self.channel.cache.set_command_context(r.requireEntity)
                if len(self.cacheEntities) <= 0:
                    self.channel.cache.set_user_context_value(
                        [e.dict() for e in self.command.entities])
                else:
                    self.channel.cache.set_user_context_value(self.cacheEntities)
                option = random.randint(0, len(r.questions) - 1)
                return ResponseModel(message=r.questions[option])
        return ResponseModel()

    def __reset_context__(self):
        self.channel.cache.clear()

    def send(self, response: ResponseModel) -> ResponseModel:
        self.__reset_context__()
        return response

    def get_entity(self, key: str) -> Optional[CommandEntity]:
        keys = [k for k in self.command.entities if k.name == key]
        if len(keys) > 0:
            return keys[0]
        return None