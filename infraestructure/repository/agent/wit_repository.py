from wit import Wit


class WitRepository:
    def __init__(self):
        self.client = Wit('FFYVNIRFYZWFVBU7L5EUTCUMGX6T3BLA')

    def get_command(self, message):
        command = {
            'text': None,
            'entities': [],
            'intents': []
        }
        nlp_resp = self.client.message(message)
        command['text'] = nlp_resp['text']
        if nlp_resp['intents'] is not None and len(nlp_resp['intents']) > 0:
            command['intents'] = [i['name'] for i in nlp_resp['intents']]

        if nlp_resp['entities'] is not None:
            entities = nlp_resp['entities']
            for e in entities:
                for ev in entities[e]:
                    command['entities'].append(
                        {"name": ev['name'], "value": ev['value']})

        return command
