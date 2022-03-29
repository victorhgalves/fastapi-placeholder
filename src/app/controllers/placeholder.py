import logging
import datetime

from fastapi import APIRouter, Request, status, Depends

from src.app.exceptions import exception_api_handler
from src.app.entities import PlaceHolderEntity
from src.app.rest.schemas import PlaceHolderSchema
from src.app.middlewares import autheticate

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/info",
        status_code=status.HTTP_200_OK,
        dependencies=[Depends(autheticate)])
@exception_api_handler
def  get_infos(request: Request) -> PlaceHolderSchema:

    response = PlaceHolderEntity.get_info()

    logger.info(f"{datetime.datetime.timestamp} - {response} - {status.HTTP_200_OK}")
    
    return response

