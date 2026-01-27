from pydantic import ConfigDict
from pydantic_settings import BaseSettings



class DBSettings(BaseSettings):
    """ Определяет настройки баз данных, которые считываются из .env файла """
    url: str

    echo: bool

    celery_broker_url: str

    celery_backend_url: str

    model_config = ConfigDict(
        extra="ignore",
        env_prefix="DB_",
    )


db_settings = DBSettings()