from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel

class Order(BaseModel):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String)
    created_at = Column(DateTime)


class OrderCreate(BaseModel):
    name: str
    status: str


class OrderUpdate(BaseModel):
    name: str
    status: str
