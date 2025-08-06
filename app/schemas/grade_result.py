from pydantic import BaseModel, Field


class GradeResult(BaseModel):
  score: int = Field(..., ge=0, le=100, description="채점 점수")
  comment: str = Field(..., description="채점 코멘트")
