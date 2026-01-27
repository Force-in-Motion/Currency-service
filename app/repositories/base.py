from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Type, Generic, cast
from sqlalchemy import select, text, delete, Table

from app.interface import ARepo
from app.tools import DatabaseError, DBModel


class BaseRepo(Generic[DBModel], ARepo):
    """
    Базовый Репозиторий.
    model должен быть определён в наследнике.
    """

    model: Type[DBModel]

    @classmethod
    async def get_all(
        cls,
        session: AsyncSession,
    ) -> Optional[list[DBModel]]:
        """
        Возвращает все модели, содержащиеся в конкретной таблице БД
        :param session: Объект асинхронной сессии
        :return: Список всех ORM моделей
        """
        try:
            stmt = select(cls.model).order_by(cls.model.id)

            result = await session.execute(stmt)

            return list(result.scalars().all())

        except SQLAlchemyError as e:
            raise DatabaseError(
                f"Error when receiving all {cls.model.__name__}s"
            ) from e

    @classmethod
    async def get_all_by_date(
        cls,
        dates: tuple[datetime, datetime],
        session: AsyncSession,
    ) -> Optional[list[DBModel]]:
        """
        Возвращает список всех модель, содержащихся в конкретной таблице БД, добавленных за указанный интервал времени
        :param session: объект асинхронной сессии
        :param dates:  кортеж, содержащий начало интервала времени и его окончание
        :return: список всех ORM моделей, добавленных за указанный интервал времени
        """
        try:
            stmt = (
                select(cls.model)
                .where(cls.model.created_at.between(*dates))
                .order_by(cls.model.created_at.desc())
            )

            result = await session.execute(stmt)

            return list(result.scalars().all())

        except SQLAlchemyError as e:
            raise DatabaseError(
                f"Error when receiving list {cls.model.__name__}s by dates"
            ) from e

    @classmethod
    async def get_last_by_name(
        cls,
        name: str,
        session: AsyncSession,
    ) -> Optional[DBModel]:
        """
        Возвращает последнюю добавленную модель в таблицы БД
        :param model_id: id модели
        :param session: объект асинхронной сессии
        :return: ORM модель по ее id
        """
        try:
            stmt = (
                select(cls.model)
                .where(cls.model.ticker == name)
                .order_by(cls.model.created_at.desc())
                .limit(1)
            )

            result = await session.execute(stmt)

            return result.scalar_one_or_none()

        except SQLAlchemyError as e:
            raise DatabaseError(
                f"Error when receiving {cls.model.__name__} by id"
            ) from e

    @classmethod
    async def clear(
        cls,
        session: AsyncSession,
    ) -> list:
        """
        Очищает таблицу БД и сбрасывает последовательность id моделей
        :param session: объект асинхронной сессии
        :return: Пустой список
        """
        table = cast(Table, cls.model.__table__)

        pk_column = next(iter(table.primary_key.columns))

        seq_name = f"{table.name}_{pk_column.name}_seq"

        try:
            await session.execute(delete(cls.model))

            await session.execute(text(f'ALTER SEQUENCE "{seq_name}" RESTART WITH 1'))

            await session.commit()

            return []

        except SQLAlchemyError as e:
            await session.rollback()
            raise DatabaseError(
                f"Error when clearing table {cls.model.__name__}"
            ) from e
