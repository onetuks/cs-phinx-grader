from pydantic import BaseModel, Field


class GradeResponse(BaseModel):
    user_answer: str = Field(..., description="제출 답안")
    best_answer: str = Field(..., description="모범 답안")
    user_score: int = Field(0, description="채점 점수")
    evaluation: str = Field("", description="훈수")
