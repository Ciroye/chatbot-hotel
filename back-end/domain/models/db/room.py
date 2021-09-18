from typing import List

from pydantic import BaseModel


class Room(BaseModel):
    code: str
    capacity: int
    price: float
    amenities: List[str]
