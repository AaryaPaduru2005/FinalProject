from pydantic import BaseModel
from datetime import date

class RevenueResponse(BaseModel):
    date: date
    total_revenue: float
