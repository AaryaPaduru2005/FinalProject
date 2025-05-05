# api/routers/orders.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from api.dependencies.database import get_db
from api.schemas.orders import OrderCreate, OrderUpdate, OrderRead, Revenue
from api.controllers.orders import (
    get_orders,
    get_order,
    create_order,
    update_order,
    delete_order,
    get_daily_revenue,
)

router = APIRouter(prefix="/orders", tags=["orders"])

# 1) Revenue route must come *before* the /{order_id} route
@router.get("/revenue/{target_date}", response_model=Revenue)
def daily_revenue(target_date: date, db: Session = Depends(get_db)):
    """
    Returns total revenue for all orders on the given date.
    """
    return get_daily_revenue(db, target_date)

@router.get("/", response_model=List[OrderRead])
def read_orders(db: Session = Depends(get_db)):
    return get_orders(db)

@router.get("/{order_id}", response_model=OrderRead)
def read_order(order_id: int, db: Session = Depends(get_db)):
    return get_order(db, order_id)

@router.post("/", response_model=OrderRead, status_code=201)
def add_order(data: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, data)

@router.put("/{order_id}", response_model=OrderRead)
def edit_order(order_id: int, data: OrderUpdate, db: Session = Depends(get_db)):
    return update_order(db, order_id, data)

@router.delete("/{order_id}", status_code=204)
def remove_order(order_id: int, db: Session = Depends(get_db)):
    delete_order(db, order_id)
