# api/models/order.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id             = Column(Integer, primary_key=True, index=True)
    customer_name  = Column(String(100), nullable=False)
    phone          = Column(String(20),  nullable=False)
    address        = Column(String(255), nullable=False)
    order_type     = Column(String(50),  nullable=True)
    promo_code     = Column(String(50),  nullable=True)
    status         = Column(String(50),  nullable=False, default="pending")
    total          = Column(Float,       nullable=False, default=0.0)
    created_at     = Column(DateTime,    nullable=False, default=datetime.utcnow)

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )
