import pytest

from app.service.service import DescriptiveAnswerGrader


@pytest.fixture(scope="session")
def grader_service():
  return DescriptiveAnswerGrader()


def test_encode_returns_tensor(grader_service):
  # Given
  question = "DB 인덱스에 대해서 설명해주세요."
  answer = "DB 인덱스는 읽기 성능을 포기하고, 그외에 삽입/갱신/삭제 기능에 특화한 기술이야."

  # When
  result = grader_service.evaluate_answer(question, answer)

  # Then
  assert isinstance(result, str), "평가 결과는 문자열이어야 합니다."


# @pytest.mark.parametrize(
#     "question,answer,expected",
#     [
#       ("DB 인덱스에 대해서 설명해주세요.",
#        "DB 인덱스는 읽기 성능을 포기하고, 그외에 삽입/갱신/삭제 기능에 특화한 기술이야.",
#        "정답"),
#       ("Python은 인터프리터 방식의 프로그래밍 언어가 맞니?",
#        "파이썬은 C++이나 자바와는 다르게 컴파일러를 사용하지 않는 인터프리터 언어입니다.",
#        "정답"),
#       ("Java는 씨 언어와는 다르게 JVM이라는 가상환경에서 구동된다.",
#        "나는 자연인이다.",
#        "잘못"),
#       ("MySQL의 기본 동시성 레벨은?",
#        "MySQL의 기본 동시성 레벨은 Serializable 이다.",
#        "잘못"),
#       ("MySQL의 기본 동시성 레벨은?",
#        "MySQL의 기본 동시성 레벨은 Repeatable Read이다.",
#        "정답")
#     ]
# )
# def test_calculate_similarity(grader_service, question, answer, expected):
#   # When
#   result = grader_service.evaluate_answer(question, answer)
#
#   # Then
#   assert expected in result, "주어진 문제에 대한 올바른 답변이 아닙니다."

def test_empty_question(grader_service):
  # Given
  question = ""
  answer = "냉장고를 부탁해"

  # When & Then
  with pytest.raises(ValueError, match="Blank question"):
    grader_service.evaluate_answer(question, answer)

def test_empty_answer(grader_service):
  # Given
  question = "DB 동시성 레벨에 대해서 말해주세요."
  answer = "    "

  # When & Then
  with pytest.raises(ValueError, match="Blank answer"):
    grader_service.evaluate_answer(question, answer)
