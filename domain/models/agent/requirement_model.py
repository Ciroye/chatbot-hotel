from pydantic import BaseModel
from typing import List


class RequirementModel(BaseModel):
    requireEntity: str
    questions: List[str]
