from typing import Optional
from abc import ABC, abstractmethod
from app.tools.types import DBModel


class ARepo(ABC):

    @classmethod
    @abstractmethod
    async def get_all(cls, *args, **kwargs) -> Optional[list[DBModel]]:
        """
        Возвращает все модели из конкретной таблицы БД
        :return: Список всех моделей | None
        """
        pass


    @classmethod
    @abstractmethod
    async def get_all_by_date(cls, *args, **kwargs) -> Optional[list[DBModel]]:
        """
        Возвращает список всех моделей, добавленных за указанный интервал времени конкретной таблицы БД
        :return: Список моделей | None
        """
        pass


    @classmethod
    @abstractmethod
    async def get_last_by_name(cls, *args, **kwargs) -> Optional[DBModel]:
        """
        Возвращает последнюю добавленную модель из конкретной таблицы БД
        :return: Модель | None
        """
        pass


    @classmethod
    @abstractmethod
    async def clear(cls, *args, **kwargs) -> list:
        """
        Очищает конкретную таблицу БД сбрасывает последовательность id моделей
        :return: Пустой список
        """
        pass
