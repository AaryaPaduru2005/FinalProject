from pydantic import BaseModel

class ReviewBase(BaseModel):
    menu_item_id: int
    rating: int
    comment: str | None = None

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        orm_mode = True
