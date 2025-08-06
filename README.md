# cs-phinx-grader

```markdown
project-root/
├── mypy.ini
├── pyproject.toml          # 프로젝트 메타데이터(의존성, 스크립트 등)
├── Dockerfile
├── docker-compose.yml
└── app/
    ├── __init__.py
    ├── main.py             # FastAPI 인스턴스 생성 및 라우터 포함
    ├── core/
    │   ├── config.py       # 환경변수 관리(BaseSettings)
    │   ├── logging.py      # 로깅 설정
    │   ├── dependencies.py # 공통 의존성(예: DB 세션)
    │   └── events.py       # startup/shutdown 이벤트 핸들러
    ├── db/
    │   ├── base.py         # SQLAlchemy Base 클래스
    │   ├── session.py      # 세션 생성 및 관리 함수
    │   └── init_db.py      # 초기 데이터 삽입 스크립트
    ├── models/
    │   └── user.py         # ORM 모델(SQLAlchemy 또는 SQLModel)
    ├── schemas/
    │   └── user.py         # Pydantic 모델(입력·출력 스키마)
    ├── crud/               # 또는 services/
    │   └── user.py         # DB 조작 및 비즈니스 로직
    ├── api/
    │   └── v1/
    │       ├── router.py   # APIRouter 인스턴스
    │       └── user.py     # 엔드포인트 정의
    └── tests/
        ├── conftest.py     # pytest 설정(예: 테스트용 DB)
        └── test_user.py    # 유닛·통합 테스트
```