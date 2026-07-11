from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    HOST: str
    PORT: int

    GEMINI_API_KEY: str = ""

    EMBEDDING_MODEL: str

    CHROMA_DB_PATH: str

    SCRAPER_BASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()