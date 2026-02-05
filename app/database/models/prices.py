from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models import Base, TimestampMixin


class Price(Base, TimestampMixin):
    """Родительский класс для всех таблицы базы данных"""

    __tablename__ = "prices"

    name: Mapped[str] = mapped_column(String, nullable=False)

    price: Mapped[str] = mapped_column(String, nullable=False)

