from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.dependencies.database import get_db
from api.schemas.review import Review, ReviewCreate, ReviewUpdate
from api.controllers.review import get_reviews, get_review, create_review, update_review, delete_review

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/", response_model=List[Review])
def read_reviews(db: Session = Depends(get_db)):
    return get_reviews(db)

@router.get("/{review_id}", response_model=Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    return get_review(db, review_id)

@router.post("/", response_model=Review, status_code=201)
def add_review(data: ReviewCreate, db: Session = Depends(get_db)):
    return create_review(db, data)

@router.put("/{review_id}", response_model=Review)
def	edit_review(review_id: int, data: ReviewUpdate, db: Session = Depends(get_db)):
    return	update_review(db, review_id, data)

@router.delete("/{review_id}", status_code=204)
def	remove_review(review_id: int, db: Session = Depends(get_db)):
    delete_review(db, review_id)
