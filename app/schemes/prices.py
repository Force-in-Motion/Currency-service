from typing import Annotated
from pydantic import BaseModel
from datetime import datetime




class PriceResponse(BaseModel):
    ticker: str
    price: str
    created_at: datetime
    updated_at: datetime


class PriceListResponse(BaseModel):
    prices: Annotated[list, PriceResponse]