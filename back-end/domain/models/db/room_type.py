from pydantic import BaseModel


class RoomType(BaseModel):
    id: int
    name: str
