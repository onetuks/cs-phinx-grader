from pydantic import BaseModel, Field


class EvaluationRequest(BaseModel):
  question: str = Field(..., min_length=1, max_length=500)
  answer: str = Field(..., min_length=1, max_length=1000)

class EvaluationResponse(BaseModel):
  is_correct: bool = Field(..., description="정답 여부")
  explanation: str = Field(..., min_length=1, max_length=500, description="해설")
  model_answer: str = Field(..., min_length=1, max_length=500, description="모범 답안")
