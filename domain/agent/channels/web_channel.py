from domain.agent.channels import BaseChannel


class WebChannel(BaseChannel):
    def __init__(self, userId):
        super().__init__(userId)
