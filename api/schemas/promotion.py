from pydantic import BaseModel
from datetime import datetime

class PromotionBase(BaseModel):
    code: str
    discount: float
    expires_at: datetime

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int
    class Config:
        orm_mode = True
