from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.order_service import get_orders, create_order, update_order, delete_order
from app.db.models import Order, OrderCreate, OrderUpdate
from typing import List

router = APIRouter()

@router.get("/orders", response_model=List[Order])
async def read_orders(db: Session = Depends(get_db)):
    return get_orders(db)

@router.post("/orders", response_model=Order)
async def add_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order_data)

@router.put("/orders/{order_id}", response_model=Order)
async def modify_order(order_id: int, order_data: OrderUpdate, db: Session = Depends(get_db)):
    return update_order(db, order_id, order_data)

@router.delete("/orders/{order_id}")
async def remove_order(order_id: int, db: Session = Depends(get_db)):
    delete_order(db, order_id)
    return {"message": "Order deleted successfully"}
