from datetime import datetime

from pydantic import BaseModel


class Reserve(BaseModel):
    code: str
    start: datetime
    end: datetime
