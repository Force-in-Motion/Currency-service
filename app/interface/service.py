from typing import Optional
from abc import ABC, abstractmethod
from app.tools.types import DBModel


class ARepo(ABC):

    @classmethod
    @abstractmethod
    async def get_all_models_table(cls, *args, **kwargs) -> Optional[list[DBModel]]:
        """
        Возвращает все модели из БД
        :return: Список всех моделей | None
        """
        pass



    @classmethod
    @abstractmethod
    async def get_last_model_in_table(cls, *args, **kwargs) -> Optional[DBModel]:
        """
        Возвращает последнюю добавленную модель из БД
        :return: Модель | None
        """
        pass


    @classmethod
    @abstractmethod
    async def get_list_models_by_date(cls, *args, **kwargs) -> Optional[list[DBModel]]:
        """
        Возвращает список всех моделей, добавленных за указанный интервал времени
        :return: Список моделей | None
        """
        pass


    @classmethod
    @abstractmethod
    async def clear_table(cls, *args, **kwargs) -> list:
        """
        Очищает БД моделей определенной категории и сбрасывает последовательность id моделей
        :return: Пустой список
        """
        pass
