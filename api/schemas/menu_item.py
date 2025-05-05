# api/schemas/menu_item.py

from typing import List, Optional
from pydantic import BaseModel

class IngredientQuantity(BaseModel):
    ingredient_id: int
    quantity_required: float

    class Config:
        orm_mode = True

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    ingredients: List[IngredientQuantity]

class MenuItemUpdate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    id: int
    ingredients: List[IngredientQuantity]

    class Config:
        orm_mode = True
