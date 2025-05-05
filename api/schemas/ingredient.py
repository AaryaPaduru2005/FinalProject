# api/schemas/ingredient.py

from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str
    unit: str | None = None
    cost_per_unit: float | None = None
    quantity_in_stock: float

class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(BaseModel):
    name: str | None = None
    unit: str | None = None
    cost_per_unit: float | None = None
    quantity_in_stock: float | None = None

class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True
