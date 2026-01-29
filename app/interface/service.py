from typing import Optional
from abc import ABC, abstractmethod
from app.tools.types import DBModel


class AService(ABC):

    @classmethod
    @abstractmethod
    async def get_all_models_from_table(cls, *args, **kwargs) -> Optional[list[DBModel]]:
        """
        Возвращает все модели из конкретной таблицы БД согласно условию
        :return: Список всех моделей | None
        """
        pass


    @classmethod
    @abstractmethod
    async def get_model_from_table(cls, *args, **kwargs) -> Optional[DBModel]:
        """
        Возвращает последнюю добавленную модель из БД согласно условию
        :return: Модель | None
        """
        pass

    
    @classmethod
    @abstractmethod
    async def register_model(cls, *args, **kwargs) -> object:
        """
        Добавляет модель в БД
        :return: Модель, добавленную в БД
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

    