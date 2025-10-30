from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration using Pydantic BaseSettings.

    Loads environment variables from .env file and provides access to project and database settings.
    """
    PROJECT_NAME: str = "Outer Ring FastAPI Base"  #: :no-index:
    API_V1_STR: str = "/api/v1"  #: :no-index:

    DB_HOST: str  #: :no-index:
    DB_PORT: int  #: :no-index:
    DB_USER: str  #: :no-index:
    DB_PASSWORD: str  #: :no-index:
    DB_NAME: str  #: :no-index:

    class Config:
        env_file = ".env"

settings = Settings()
