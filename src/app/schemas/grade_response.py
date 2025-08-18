from typing import List

from pydantic import BaseModel, Field


class GradeResponse(BaseModel):
    user_answer: str = Field(..., description="제출답안", alias="userAnswer")
    desirable_answers: List[str] = Field(..., description="모범 답안", alias="desirableAnswers")
    best_score: int = Field(0, description="채점점수", alias="bestScore")
    best_answer: str = Field(..., description="모범답안", alias="bestAnswer")

    class Config:
        validate_by_name = True
