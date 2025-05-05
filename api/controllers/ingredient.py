# api/controllers/ingredient.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.ingredient import Ingredient
from api.schemas.ingredient import IngredientCreate, IngredientUpdate

def get_ingredients(db: Session):
    return db.query(Ingredient).all()

def get_ingredient(db: Session, ingredient_id: int):
    ing = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ing:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ing

def create_ingredient(db: Session, data: IngredientCreate):
    ing = Ingredient(
        name=data.name,
        unit=data.unit,
        cost_per_unit=data.cost_per_unit,
        quantity_in_stock=data.quantity_in_stock
    )
    db.add(ing)
    db.commit()
    db.refresh(ing)
    return ing

def update_ingredient(db: Session, ingredient_id: int, data: IngredientUpdate):
    ing = get_ingredient(db, ingredient_id)
    for field, value in data.dict(exclude_unset=True).items():
        setattr(ing, field, value)
    db.commit()
    db.refresh(ing)
    return ing

def delete_ingredient(db: Session, ingredient_id: int):
    ing = get_ingredient(db, ingredient_id)
    db.delete(ing)
    db.commit()
