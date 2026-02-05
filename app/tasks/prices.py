from app.core.celery import celery
from app.services import PriceService
from app.tools.helpers import run_async




@celery.task(name="app.tasks.prices.fetch_price_task")
@run_async
async def fetch_price_task(currency_name: str) -> None:
    """
    Асинхронная фоновая задача на получение данных с Derbit API 
    :param param: название валюты 
    :return: None
    """
    await PriceService.fetch_and_register_currency_model(currency_name)


