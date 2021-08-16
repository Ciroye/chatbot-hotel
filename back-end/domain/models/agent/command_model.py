from pydantic import BaseModel
from typing import List


class CommandEntity(BaseModel):
    name: str
    value: str


class CommandModel(BaseModel):
    text: str
    intents: List[str]
    entities: List[CommandEntity]
