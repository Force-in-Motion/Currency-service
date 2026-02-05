from typing import Optional
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from app.tools import HTTPErrors
from app.services import PriceService
from app.database.models import Price as Price_model


class PriceDepends:

    @classmethod
    async def get_history_price_by_name_currency(
        cls,
        ticker: str,
        session: AsyncSession,
        dates: Optional[tuple[datetime, datetime]] = None,
    ) -> list[Price_model]:
        """
        Возвращает историю цены конкретной валюты в зависимости от переданных аргументов
        :param session: Асинхронная сессия
        :param ticker: Название валюты
        :param dates: Опциональный параметр dates - кортеж,
        содержащий начало интервала времени и его окончание
        :return: Список моделей стоимостей
        """
        models = await PriceService.get_all_models_from_table(
            name=ticker,
            dates=dates,
            session=session,
        )

        if not models:
            raise HTTPErrors.not_found

        return models


    @classmethod
    async def get_currency_price_by_name(
        cls,
        ticker: str,
        session: AsyncSession,
        last: Optional[bool] = False,
    ) -> Price_model:
        """
        Возвращает конкретную модель стоимости  в зависимости от переданных аргументов
        :param ticker: Название валюты
        :param session: Асинхронная сессия
        :param last: Флаг, определяющий способ поиска
        :return: Модель стоимости
        """
        model = await PriceService.get_model_from_table(
            name=ticker,
            last=last,
            session=session,
        )

        if not model:
            raise HTTPErrors.not_found

        return model
