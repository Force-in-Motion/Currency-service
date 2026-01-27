from app.repositories import BaseRepo
from app.database.models import Price


class PriceRepo(BaseRepo[Price]):
    """ Репозиторий, работающий с моделью Price """
    
    model = Price