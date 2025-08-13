from dataclasses import asdict

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api import router
from app.core.config import conf


def init_app():
    instance = FastAPI()

    # 환경 정의
    conf_dict = asdict(conf())
    instance.state.config = conf_dict

    # 미들웨어 정의
    instance.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 라우터 정의
    instance.include_router(router)

    return instance


app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
