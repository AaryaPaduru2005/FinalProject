from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id                = Column(Integer, primary_key=True, index=True)
    name              = Column(String(100), nullable=False)
    unit              = Column(String(50), nullable=False)
    cost_per_unit     = Column(Float, nullable=False)
    quantity_in_stock = Column(Float, nullable=False)

    # must match back_populates on MenuItemIngredient.ingredient
    menu_item_ingredients = relationship(
        "MenuItemIngredient",
        back_populates="ingredient",
        cascade="all, delete-orphan"
    )
