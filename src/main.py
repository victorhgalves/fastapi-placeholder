from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.controllers import api_router

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from starlette.middleware import Middleware


middlewares = [
    Middleware(CORSMiddleware,
    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
]

app = FastAPI(title="app",
            openapi_url="/api/v1/openapi.json",
            middleware=middlewares)

limiter = Limiter(key_func=get_remote_address)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.include_router(api_router)