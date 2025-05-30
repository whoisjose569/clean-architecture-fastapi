from fastapi import FastAPI
from src.main.routes.routes import user_router
from src.errors.error_handler import http_error_handler
from src.errors.types.base import HttpError

app = FastAPI()

app.include_router(user_router)
app.add_exception_handler(HttpError, http_error_handler)
