from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from app.core.config import db_settings


class SessionMaker:
    """Ключевой объект приложения, создающий подключение к БД, фабрику сессий и управляет сиссиями"""

    def __init__(self, url: str, echo: bool):
        self.__engine = create_async_engine(
            url=url,
            echo=echo,
            poolclass=NullPool,
        )

        self.__session_factory = async_sessionmaker(
            bind=self.__engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Асинхронный генератор, который предоставляет сессию для маршрутов и автоматически закрывает её после использования.
        :return: AsyncSession
        """
        async with self.__session_factory() as session:
            yield session


    @asynccontextmanager
    async def session_scope(self):
        """
        Асинхронный контекстный менеджер, который предоставляет сессию celery и автоматически закрывает её после использования.
        :return: AsyncSession
        """
        async with self.__session_factory() as session:
            yield session



db_connector = SessionMaker(
    url=db_settings.url,
    echo=db_settings.echo,
)