from pydantic import BaseModel
from src.app.services import PlaceHolderService
from pydantic import BaseModel


class PlaceHolderEntity(BaseModel):
    @classmethod
    def get_info(cls):
        info = PlaceHolderService.get_information()
        return info