from typing import Annotated
from datetime import datetime
from fastapi import APIRouter, Query, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemes import PriceListResponse, PriceResponse
from app.database.session import db_connector
from app.api.depends import Inspector, PriceDepends


router = APIRouter(prefix="/price", tags=["Pcice currency in USDT"])


@router.get(
    "/all",
    response_model=PriceListResponse,
    status_code=status.HTTP_200_OK,
)
async def get_all_history_currency_price(
    ticker: Annotated[str, Query(..., description="Inpun Currency name")],
    session: Annotated[AsyncSession, Depends(db_connector.get_session)],
) -> PriceListResponse:
    """
    Обрабатывает запрос на получение всей истории стоимости конкретной валюты
    :param session: Асинхронная сессия
    :return:
    """
    price_models = await PriceDepends.get_history_price_by_name_currency(
        ticker=ticker,
        session=session,
    )

    return PriceListResponse(prices=price_models)


@router.get(
    "/date",
    response_model=PriceListResponse,
    status_code=status.HTTP_200_OK,
)
async def get_history_currency_price_by_date(
    session: Annotated[AsyncSession, Depends(db_connector.get_session)],
    dates: Annotated[tuple[datetime, datetime], Depends(Inspector.date_checker)],
    ticker: Annotated[str, Query(..., description="Inpun Currency name")],
) -> PriceListResponse:
    """
    Обрабатывает запрос с fontend на получение всех добавленных в БД пользователей за указанный интервал времени
    :param dates:  кортеж, содержащий начало интервала времени и его окончание
    :param session: объект сессии, который получается путем выполнения зависимости (метода get_session объекта db_connector)
    :return: Список пользователей в виде Pydantic схем за указанную дату в виде Pydantic схем
    """
    price_models = await PriceDepends.get_history_price_by_name_currency(
        dates=dates,
        ticker=ticker,
        session=session,
    )

    return PriceListResponse(prices=price_models)


@router.get("/", response_model=PriceResponse, status_code=status.HTTP_200_OK)
async def get_last_currency_price(
    ticker: Annotated[str, Query(..., description="Inpun Currency name")],
    session: Annotated[AsyncSession, Depends(db_connector.get_session)],
) -> PriceResponse:
    """
    Обрабатывает запрос на получение последней стоимости конкретной валюты
    :param session: Асинхронная сессия
    :return:
    """
    price_model = await PriceDepends.get_currency_price_by_name(
        last=True,
        ticker=ticker,
        session=session,
    )

    return price_model
