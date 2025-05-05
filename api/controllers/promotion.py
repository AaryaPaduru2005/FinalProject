from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.promotion import Promotion
from api.schemas.promotion import PromotionCreate, PromotionUpdate
from datetime import datetime

def get_promotions(db: Session):
    return db.query(Promotion).all()

def get_promotion(db: Session, promo_id: int):
    promo = db.query(Promotion).filter(Promotion.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promo

def create_promotion(db: Session, data: PromotionCreate):
    promo = Promotion(
        code=data.code,
        discount=data.discount,
        expires_at=data.expires_at
    )
    db.add(promo)
    db.commit()
    db.refresh(promo)
    return promo

def update_promotion(db: Session, promo_id: int, data: PromotionUpdate):
    promo = get_promotion(db, promo_id)
    for field, value in data.dict(exclude_unset=True).items():
        setattr(promo, field, value)
    db.add(promo)
    db.commit()
    db.refresh(promo)
    return promo

def delete_promotion(db: Session, promo_id: int):
    promo = get_promotion(db, promo_id)
    db.delete(promo)
    db.commit()
