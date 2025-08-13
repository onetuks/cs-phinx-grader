from fastapi import APIRouter
from starlette.responses import Response

from src.app.schemas.grade_request import GradeRequest
from src.app.schemas.grade_response import GradeResponse
from src.app.schemas.grade_result import GradeResult
from src.app.service.service import GradeService

router = APIRouter()

grade_service = GradeService()


@router.get("/")
async def health():
    return Response("Welcome CSPhinx Grader API Server", status_code=200)


@router.put(
    "/api/grader",
    response_model=GradeResponse,
    description="제출답변과 모범답안목록을 받아 채점점수, 근사한 모범답안을 반환",
)
async def grade_user_answer(grade_request: GradeRequest):
    """
    질문과 답변을 평가하고 결과를 반환하는 API
    """
    result: GradeResult = grade_service.grade(grade_request.user_answer, grade_request.desirable_answers)

    return GradeResponse(
        user_answer=grade_request.user_answer,
        desirable_answers=grade_request.desirable_answers,
        best_score=result.best_score,
        best_answer=result.best_answer,
    )
