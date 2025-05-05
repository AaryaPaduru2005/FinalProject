# api/schemas/orders.py

from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional

class OrderItemBase(BaseModel):
    menu_item_id: int
    quantity: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    customer_name: str
    phone: str
    address: str
    order_type: Optional[str] = None
    promo_code: Optional[str] = None

class OrderCreate(OrderBase):
    items: List[OrderItemBase]

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    tracking_number: Optional[str] = None  # if you track shipments

    class Config:
        orm_mode = True

class OrderRead(OrderBase):
    id: int
    status: str
    total: float
    created_at: datetime
    items: List[OrderItemBase]

    class Config:
        orm_mode = True

class Revenue(BaseModel):
    date: date
    total_revenue: float

    class Config:
        orm_mode = True
