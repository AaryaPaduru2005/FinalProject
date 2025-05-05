from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class MenuItemIngredient(Base):
    __tablename__ = "menu_item_ingredients"

    id                = Column(Integer, primary_key=True, index=True)
    menu_item_id      = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    ingredient_id     = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    quantity_required = Column(Float, nullable=False)

    # must match back_populates on Ingredient.menu_item_ingredients
    ingredient = relationship(
        "Ingredient",
        back_populates="menu_item_ingredients"
    )
    # keep your existing menu_item ↔ recipe mapping
    menu_item = relationship(
        "MenuItem",
        back_populates="recipe"
    )
