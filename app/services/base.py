from datetime import datetime
from typing import Type, Generic, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from app.interface.service import AService
from app.tools.types import DBModel, Repo


class BaseService(Generic[Repo], AService):

    repo: Type[Repo]

    @classmethod
    async def get_all_models_from_table(
        cls,
        session: AsyncSession,
        dates: Optional[datetime] = None,
    ) -> Optional[list[DBModel]]:
        """
        TODO: Оркестрация вариантов поиска
        Возвращает все модели согласно полученым параметрам
        :param session: Асинхронная сессия
        :param dates: Опциональный параметр dates - кортеж,
        содержащий начало интервала времени и его окончание
        :return: Список всех ORM моделей | None
        """
        if dates is not None:
            return await cls.repo.get_all(
                session=session,
            )

        return cls.repo.get_all_by_date(
            session=session,
            dates=dates,
        )

    @classmethod
    async def get_model_from_table(
        cls,
        session: AsyncSession,
        name: Optional[str] = None,
        last: bool = False,
    ) -> Optional[DBModel]:
        """
        TODO: Оркестрация вариантов поиска
        Возвращает модель согласно полученым параметрам
        :param session: Асинхронная сессия
        :param user_id: Опциональный параметр, id пользователя
        :param model_id: Опциональный параметр, id  модели
        :return: ORM Модель | None
        """
        if last is not None:
            return await cls.repo.get_last_by_name(
                name=name,
                session=session,
            )

        # TODO: Подразумевается что метод может расширяться и будут добавлены варианты поиска модели


    @classmethod
    async def clear_table(
        cls,
        session: AsyncSession,
    ) -> list:
        """
        Очищает таблицу БД
        :param session: объект асинхронной сессии
        :return: Пустой список
        """
        return await cls.repo.clear(session=session)
