from abc import ABCMeta
from infraestructure.utils import Config


class BaseChannel(metaclass=ABCMeta):
    def __init__(self):
        # config = Config().get_config(section='redis')
        # Cache server goes here
        self.cache = None
        self.context: str = None
