from sqlalchemy import Column, Integer, String, Float, DateTime
from api.dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False)
    discount = Column(Float, nullable=False)
    expires_at = Column(DateTime, nullable=False)
