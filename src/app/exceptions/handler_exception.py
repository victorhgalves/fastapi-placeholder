from fastapi import HTTPException
from functools import wraps
from .business_exception import BusinessException
from src.app.rest.http_errors import http_error_handle
import logging


def exception_api_handler(func):
    logger = logging.getLogger(func.__name__)
    @wraps(func)
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"An error occurred on endpoint: {func.__name__}, Error {e}")
            if isinstance(e, BusinessException):
                if not http_error_handle.dict_errors.get(str(e)) is None:
                    raise http_error_handle.dict_errors.get(str(e))

            raise HTTPException(status_code=500, detail="Internal Server Error")
    return inner_function

