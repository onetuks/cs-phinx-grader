from fastapi import APIRouter
from starlette.responses import Response

from app.schemas.grade_request import GradeRequest
from app.schemas.grade_response import GradeResponse
from app.schemas.grade_result import GradeResult
from app.service.service import GradeService

router = APIRouter()

grade_service = GradeService()


@router.get("/")
async def health():
  return Response("Welcome CSPhinx Grader API Server", status_code=200)

@router.put("/api/grader", response_model=GradeRequest)
async def grade_user_answer(grade_request: GradeRequest) -> GradeResponse:
  """
  질문과 답변을 평가하고 결과를 반환하는 API
  """
  result: GradeResult = grade_service.grade(
      grade_request.user_answer,
      grade_request.desirable_answers)

  return GradeResponse(
      user_score=result.score,
      grade_comment=result.comment,
  )
