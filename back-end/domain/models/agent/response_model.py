from pydantic import BaseModel
from typing import List


class ResponseModel(BaseModel):
    message: str = ""
