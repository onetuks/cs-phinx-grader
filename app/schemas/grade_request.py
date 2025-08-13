from typing import List

from pydantic import BaseModel, Field


class GradeRequest(BaseModel):
    user_answer: str = Field(..., description="제출답안")
    desirable_answers: List[str] = Field(..., description="모범답안")
