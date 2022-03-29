import requests

from src.app.config import PLACEHOLDER_API
from src.app.rest.schemas import PlaceHolderSchema

class PlaceHolderService:
    @staticmethod
    def get_information():
        requests_url = f"{PLACEHOLDER_API}/todos"

        response = requests.get(requests_url).json()[:5]

        return PlaceHolderSchema(__root__=response)