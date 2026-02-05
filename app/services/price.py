import httpx

from app.schemes.prices import PriceRequest
from app.services import BaseService
from app.repositories import PriceRepo
from app.core.config import deribit_settings
from app.database.session import db_connector


class PriceService(BaseService[PriceRepo]):

    repo = PriceRepo

    @classmethod
    async def _fetch_price(cls, currency_name: str) -> PriceRequest:
        """
        Служебный метод, выполняет get запрос на Derbit API для получения данных о конкретной валюте
        :param currency_name: Название валюты
        :return: Сформированную PD Схему с полученными данными
        """
        async with httpx.AsyncClient(timeout=deribit_settings.timeout) as client:

            response = await client.get(
                deribit_settings.url,
                params={"instrument_name": currency_name},
            )

            response.raise_for_status()

            data = response.json()

            return PriceRequest(
                name=currency_name,
                price=str(data["result"]["index_price"]),
            )

    @classmethod
    async def fetch_and_register_currency_model(cls, currency_name) -> None:
        """
        Получает данные с Derbit API и записывает их в БД
        :param currency_name: Название валюты
        :return:
        """
        currency_scheme = await cls._fetch_price(currency_name)

        async with db_connector.session_scope() as session:
            await cls.register_model(
                scheme_in=currency_scheme,
                session=session
            )
            