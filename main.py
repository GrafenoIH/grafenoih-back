from fastapi import FastAPI
from app.controllers.controller import router

app = FastAPI()

app.include_router(router)

