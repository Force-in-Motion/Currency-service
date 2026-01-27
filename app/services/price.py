from app.services import BaseService
from app.repositories import PriceRepo


class TokenService(BaseService[PriceRepo]):

    repo = PriceRepo