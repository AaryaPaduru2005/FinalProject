from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(100), nullable=False)
    description = Column(String(255))
    price       = Column(Float, nullable=False)
    category    = Column(String(50))

    # must match back_populates on MenuItemIngredient.menu_item
    recipe      = relationship(
        "MenuItemIngredient",
        back_populates="menu_item",
        cascade="all, delete-orphan"
    )
    order_items = relationship("OrderItem", back_populates="menu_item")
    reviews     = relationship("Review", back_populates="menu_item")
