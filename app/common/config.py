import logging
from dataclasses import dataclass
from os import path, environ

base_dir = path.dirname(path.dirname(path.abspath(__file__)))

@dataclass
class Config:
  BASE_DIR = base_dir

  logging.basicConfig(level=logging.INFO)

@dataclass
class LocalConfig(Config):
  PROJ_RELOAD: bool = True

@dataclass
class ProdConfig(Config):
  PROJ_RELOAD: bool = False


def conf():
  """ 환경 불러오기 """
  config = dict(prod=ProdConfig(), local=LocalConfig())
  return config.get(environ.get("API_ENV", "local"))
