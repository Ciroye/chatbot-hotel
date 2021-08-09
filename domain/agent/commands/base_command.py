from __future__ import annotations
from abc import ABCMeta, abstractmethod
from domain.models.agent import CommandModel, ResponseModel, RequirementModel, CommandEntity
from domain.agent.channels import BaseChannel
from typing import List
import random


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
        return self.command_intent in self.command.intents or self.__is_context_action()

    def meet_requirements(self) -> bool:
        if self.__is_context_action():
            self.cacheEntities = self.__fill_entities()
        entities = [e.name for e in self.command.entities if e.name and e.value]
        for r in self.requirements:
            if r.requireEntity not in entities:
                return False
        return True

    def __is_context_action(self):
        print(self.channel.context)
        return self.command_intent == self.channel.context

    def __fill_entities(self):
        self.__check_command_step()
        entities = self.channel.get_user_context_value()
        if entities:
            print(entities)
            for e in entities:
                self.command.entities.append(CommandEntity(**e))
            return entities
        return []

    def __check_command_step(self):
        commandStep = self.channel.get_command_context()
        if commandStep:
            entities = entities = self.channel.get_user_context_value()
            if entities:
                entities.append(
                    {"name": commandStep, "value": self.command.text})
            else:
                entities = [{"name": commandStep, "value": self.command.text}]
            self.channel.set_user_context_value(entities)

    def ask_for_requirements(self) -> ResponseModel:
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
        return ResponseModel()

    def __reset_context(self):
        self.channel.clear()

    def sed(self, response: ResponseModel) -> ResponseModel:
        self.__reset_context()
        return response
