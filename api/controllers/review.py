from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.review import Review
from api.schemas.review import ReviewCreate, ReviewUpdate

def get_reviews(db: Session):
    return db.query(Review).all()

def get_review(db: Session, review_id: int):
    rv = db.query(Review).filter(Review.id == review_id).first()
    if not rv:
        raise HTTPException(status_code=404, detail="Review not found")
    return rv

def create_review(db: Session, data: ReviewCreate):
    rv = Review(
        menu_item_id=data.menu_item_id,
        rating=data.rating,
        comment=data.comment
    )
    db.add(rv)
    db.commit()
    db.refresh(rv)
    return rv

def update_review(db: Session, review_id: int, data: ReviewUpdate):
    rv = get_review(db, review_id)
    for field, value in data.dict(exclude_unset=True).items():
        setattr(rv, field, value)
    db.add(rv)
    db.commit()
    db.refresh(rv)
    return rv

def delete_review(db: Session, review_id: int):
    rv = get_review(db, review_id)
    db.delete(rv)
    db.commit()
