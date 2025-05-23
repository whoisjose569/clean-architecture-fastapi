from fastapi import FastAPI
from src.main.routes.routes import user_router

app = FastAPI()

app.include_router(user_router)
