from fastapi import FastAPI
from app.api.v1.orders import router as orders_router

app = FastAPI()

app.include_router(orders_router, prefix="/api/v1")
