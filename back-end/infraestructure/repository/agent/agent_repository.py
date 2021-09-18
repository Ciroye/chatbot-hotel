import json


class AgentRepository:
    def __init__(self):
        with open("data.json") as json_file:
            self.db = json.load(json_file)

    def get_rooms(self):
        return self.db['rooms']

    def get_reserves(self):
        return self.db['reserves']
