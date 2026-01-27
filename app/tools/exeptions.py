from fastapi import HTTPException, status


class DatabaseError(Exception):
    """Ошибка работы с базой данных."""

    pass


class HTTPErrors(Exception):
    """Ошибка нахождения данных."""

    db_error = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Database operation error",
    )

    not_found = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Data not found",
    )

    bad_request = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Bad request",
    )

    clear_table = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Error cleared table",
    )
