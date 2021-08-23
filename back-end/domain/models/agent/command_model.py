from typing import List, Optional

from pydantic import BaseModel


class CommandDates(BaseModel):
    from_: str
    to: str


class CommandEntity(BaseModel):
    name: str
    value: Optional[str]
    dates: Optional[CommandDates]


class CommandModel(BaseModel):
    text: str
    intents: List[str]
    entities: List[CommandEntity]
