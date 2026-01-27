from typing import TypeVar, TYPE_CHECKING


if TYPE_CHECKING:
    from pydantic import BaseModel
    from app.interface import ARepo
    from app.database.models import Base


# Абстрактные типы модели, схемы, репозитория
DBModel = TypeVar(name="DBModel", bound="Base")
Repo = TypeVar(name="Repo", bound="ARepo")
PDScheme = TypeVar(name="PDScheme", bound="BaseModel")
