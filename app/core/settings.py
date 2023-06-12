from pydantic import BaseSettings
from environs import Env

env = Env()
env.read_env()


class MongoDBSettings(BaseSettings):
    DB_HOST: str = env("MONGO_HOST")
    DB_PORT: int = env("MONGO_PORT")
    DB_DATABASE: str = env("MONGO_DB")

    DB_URL: str = f"mongodb://{DB_HOST}:{DB_PORT}"

    class Config:
        case_sensitive = True


class Settings(BaseSettings):
    # But try MONGO_DB
    MONGO_DB: MongoDBSettings = MongoDBSettings()
