from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class PriceRequest(BaseModel):
    ticker: str
    price: str


class PriceResponse(PriceRequest):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime


class PriceListResponse(BaseModel):
    prices: List[PriceResponse]