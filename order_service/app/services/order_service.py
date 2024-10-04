from http.client import HTTPException

from sqlalchemy.orm import Session
from app.db.models import Order, OrderUpdate


def get_orders(db: Session):
    return db.query(Order).all()


def create_order(db: Session, order_data: dict):
    order = Order(**order_data.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def update_order(db: Session, order_id: int, order_data: OrderUpdate):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    for key, value in order_data.dict().items():
        setattr(order, key, value)
    db.commit()
    db.refresh(order)

    return order


def delete_order(db:Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
