from abc import ABCMeta

from infraestructure.repository.agent import CacheRepository


class BaseChannel(metaclass=ABCMeta):
    def __init__(self):
        self.cache = CacheRepository()
        self.context: str = self.cache.get_user_context()
