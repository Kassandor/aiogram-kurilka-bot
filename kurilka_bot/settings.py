from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки приложения
    """

    TELEGRAM_TOKEN: str = Field(default='')
    POLL_SMOKE_COLDOWN_MINUTES: int = Field(default=50)
    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
