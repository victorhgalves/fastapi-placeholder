from fastapi import APIRouter

from .healthcheck import router as router_healthcheck
from .placeholder import router as router_placeholder

api_router = APIRouter()
api_router.include_router(router_healthcheck, tags=["healthcheck"])
api_router.include_router(router_placeholder, prefix="/placeholder", tags=["placeholder"])