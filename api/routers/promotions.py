from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.dependencies.database import get_db
from api.schemas.promotion import Promotion, PromotionCreate, PromotionUpdate
from api.controllers.promotion import get_promotions, get_promotion, create_promotion, update_promotion, delete_promotion

router = APIRouter(prefix="/promotions", tags=["promotions"])

@router.get("/", response_model=List[Promotion])
def read_promotions(db: Session = Depends(get_db)):
    return get_promotions(db)

@router.get("/{promo_id}", response_model=Promotion)
def read_promotion(promo_id: int, db: Session = Depends(get_db)):
    return get_promotion(db, promo_id)

@router.post("/", response_model=Promotion, status_code=201)
def add_promotion(data: PromotionCreate, db: Session = Depends(get_db)):
    return create_promotion(db, data)

@router.put("/{promo_id}", response_model=Promotion)
def edit_promotion(promo_id: int, data: PromotionUpdate, db: Session = Depends(get_db)):
    return update_promotion(db, promo_id, data)

@router.delete("/{promo_id}", status_code=204)
def remove_promotion(promo_id: int, db: Session = Depends(get_db)):
    delete_promotion(db, promo_id)
