from pathlib import Path
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    """Определяет настройки БД, которые считываются из .env файла"""

    url: str

    echo: bool

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="DB_",
    )


class DeribitSettings(BaseSettings):
    """Настройки Deribit API, которые считываются из .env файла"""

    url: str

    timeout: int

    btc_instrument: str

    eth_instrument: str

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="DERIBIT_",
    )


class CelerySettings(BaseSettings):

    beat_interval: int

    broker_url: str

    backend_url: str

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="CELERY_",
    )


db_settings = DBSettings()

celery_settings = CelerySettings()

deribit_settings = DeribitSettings()
