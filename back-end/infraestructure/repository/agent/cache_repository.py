import json

from redis import Redis

from infraestructure.utils import Config


class CacheRepository:
    def __init__(self):
        config = Config().get_config(section='redis')
        self.cache = Redis(host=config['host'], db=int(config['db']), port=int(config['port']), decode_responses=True)

    def get_user_context(self):
        return str(self.cache.get('_context_'))

    def set_user_context(self, value):
        return self.cache.set('_context_', value)

    def set_command_context(self, value: str):
        return self.cache.set('_command_context_', value)

    def get_command_context(self):
        return str(self.cache.get('_command_context_'))

    def get_user_context_value(self):
        value = self.cache.get('_context_value_')
        if value:
            return json.loads(value)
        return None

    def set_user_context_value(self, value):
        return self.cache.set('_context_value_', json.dumps(value))

    def clear(self):
        self.cache.delete('_context_', '_command_context_', '_context_value_')
