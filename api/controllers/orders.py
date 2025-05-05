# api/controllers/orders.py

from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date
from datetime import date, datetime
from fastapi import HTTPException

from api.models.order import Order as OrderModel
from api.models.order_item import OrderItem as OrderItemModel
from api.schemas.orders import OrderCreate, OrderUpdate

def get_orders(db: Session):
    return db.query(OrderModel).all()

def get_order(db: Session, order_id: int):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

def create_order(db: Session, data: OrderCreate):
    # 1) Create order skeleton
    order = OrderModel(
        customer_name=data.customer_name,
        phone=data.phone,
        address=data.address,
        order_type=data.order_type,
        promo_code=data.promo_code,
        status="pending",
        total=0.0,
        created_at=datetime.utcnow()
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    # 2) Attach items and accumulate total
    total = 0.0
    for item in data.items:
        oi = OrderItemModel(
            order_id=order.id,
            menu_item_id=item.menu_item_id,
            quantity=item.quantity
        )
        db.add(oi)
        total += oi.quantity * oi.menu_item.price
    order.total = total
    db.commit()
    db.refresh(order)
    return order

def update_order(db: Session, order_id: int, data: OrderUpdate):
    order = get_order(db, order_id)
    updates = data.dict(exclude_unset=True)
    for k, v in updates.items():
        setattr(order, k, v)
    db.commit()
    db.refresh(order)
    return order

def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    db.delete(order)
    db.commit()

def get_daily_revenue(db: Session, target_date: date):
    total = (
        db.query(func.sum(OrderModel.total))
          .filter(cast(OrderModel.created_at, Date) == target_date)
          .scalar()
        or 0.0
    )
    return {"date": target_date, "total_revenue": float(total)}
