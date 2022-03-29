from typing import List
from pydantic import BaseModel


class PlaceHolderInfos(BaseModel):
    id: int
    title: str

class PlaceHolderSchema(BaseModel):
    __root__: List[PlaceHolderInfos]
