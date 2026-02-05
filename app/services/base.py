from datetime import datetime
from typing import Type, Generic, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from app.interface.service import AService
from app.tools import DBModel, PDScheme, Repo


class BaseService(Generic[Repo], AService):

    repo: Type[Repo]

    @classmethod
    async def get_all_models_from_table(
        cls,
        session: AsyncSession,
        name: Optional[str] = None,
        dates: Optional[tuple[datetime, datetime]] = None,
    ) -> list[DBModel]:
        """
        TODO: Оркестрация вариантов поиска
        Возвращает все модели согласно полученым параметрам
        :param session: Асинхронная сессия
        :param name: Опциональный параметр name - название модели,
        :param dates: Опциональный параметр dates - кортеж,
        содержащий начало интервала времени и его окончание
        :return: Список всех ORM моделей | []
        """
        if dates is None:
            return await cls.repo.get_all_by_name(
                name=name,
                session=session,
            )

        return await cls.repo.get_all_by_date(
            name=name,
            dates=dates,
            session=session,
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
        if last:
            return await cls.repo.get_last_by_name(
                name=name,
                session=session,
            )

        # TODO: Подразумевается что метод может расширяться и будут добавлены варианты поиска модели

    @classmethod
    async def register_model(
        cls,
        scheme_in: PDScheme,
        session: AsyncSession,
    ) -> DBModel:
        """
        Регистрирует модель в БД согласно полученым параметрам
        :param scheme_in: Pydantic схема - объект, содержащий данные для регистрации модели
        :param user_id: Опциональный параметр, id пользователя
        :param session: Асинхронная сессия
        :return: Зарегистрированную ORM модель
        """

        data = scheme_in.model_dump()

        return await cls.repo.create(
            model=cls.repo.model(**data),
            session=session,
        )

    @classmethod
    async def clear_table(
        cls,
        session: AsyncSession,
    ) -> list:
        """
        Очищает таблицу БД
        :param session: объект асинхронной сессии
        :return: []
        """
        return await cls.repo.clear(session=session)
