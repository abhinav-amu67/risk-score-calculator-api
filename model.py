from pydantic import BaseModel
from typing import List


class Violation(BaseModel):
    type: str
    severity: float


class InputData(BaseModel):
    violations: List[Violation]
