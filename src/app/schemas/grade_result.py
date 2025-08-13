from pydantic import BaseModel, Field


class GradeResult(BaseModel):
    best_score: int = Field(..., ge=0, le=100, description="채점점수")
    best_answer: str = Field(..., description="근사한 모범답안")
