import uvicorn
from fastapi import FastAPI

from app.common.config import conf
from app.routes import index


def init_app():
  instance = FastAPI()

  # 환경 정의
  # config = conf()
  # conf_dict = asdict(config)

  # 미들웨어 정의

  # 라우터 정의
  instance.include_router(index.router)

  return instance


app = init_app()

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
