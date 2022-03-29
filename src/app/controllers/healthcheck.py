import time
from fastapi import APIRouter
from src.app.version import __version__

router = APIRouter()

@router.get("/readiness")
def get_ping():
    return {"live": True, "version": __version__}
