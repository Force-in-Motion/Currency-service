from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from app.core.config import db_settings


class SessionMaker:
    """ Ключевой объект приложения, создающий подключение к БД, фабрику сессий и управляет сиссиями """

    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Асинхронный контекстный менеджер, который предоставляет сессию для маршрутов и автоматически закрывает её после использования.
        :return: AsyncSession
        """
        async with self.session_factory() as session:
            yield session


db_connector = SessionMaker(url=db_settings.url, echo=db_settings.echo)
