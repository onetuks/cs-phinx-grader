from fastapi import APIRouter, Request
from starlette.responses import Response

from app.model.models import EvaluationResponse, EvaluationRequest

router = APIRouter()


@router.get("/")
async def health():
  return Response("Welcome CSPhinx Grader API Server", status_code=200)

@router.get("/evaluations", response_model=EvaluationResponse)
async def get_evaluation(request: Request, evaluation_request: EvaluationRequest) -> EvaluationResponse:
  """
  질문과 답변을 평가하고 결과를 반환하는 API
  """
  evaluation_result = request.app.state.grader_service.evaluate_answer(
      evaluation_request.question, evaluation_request.answer)

  return EvaluationResponse(
      is_correct=True,
      explanation=evaluation_result,
      model_answer="모범답안",
  )
