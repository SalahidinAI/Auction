from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class CarListValidate(BaseModel):
    id: int
    category: str
    marka: str
    model: str
    price: int
    year: date
    mileage: int
    city: str
    country: str
    with_photo: bool
    color: str
    volume: float
    description: Optional[str] = None


class CarBetValidate(BaseModel):
    id: int
    number: int
    total_number: int
    buy_now: int
    start_date: datetime
    end_date: datetime
