from abc import ABCMeta, abstractmethod
from redis import Redis
from infraestructure.utils import Config
import json


class BaseChannel(metaclass=ABCMeta):
    def __init__(self, userId: int):
        config = Config().get_config(section='redis')
        self.cache = Redis(host=config['host'], db=int(
            config['db']), port=int(config['port']), decode_responses=True)
        self.context: str = None
        self.userId = userId
        self.__get_user_context()

    def __get_user_context(self):
        self.context = str(self.cache.get(f'{self.userId}_context'))

    def set_user_context(self, value):
        return self.cache.set(f'{self.userId}_context', value)

    def set_command_context(self, value: str):
        return self.cache.set(f'{self.userId}_command_context', value)

    def get_command_context(self):
        return str(self.cache.get(f'{self.userId}_command_context'))

    def get_user_context_value(self):
        value = self.cache.get(f'{self.userId}_context_value')
        if value:
            return json.loads(value)
        return None

    def set_user_context_value(self, value):
        return self.cache.set(f'{self.userId}_context_value', json.dumps(value))

    def clear(self):
        self.cache.delete(f'{self.userId}_context',
                          f'{self.userId}_command_context', f'{self.userId}_context_value')
