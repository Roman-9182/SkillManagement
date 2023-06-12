from app.core.settings import Settings
from functools import lru_cache


@lru_cache()
def get_setting() -> Settings:
    return Settings()


config: Settings = get_setting()
