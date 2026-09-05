from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class HotelOfferRecord(BaseModel):
    hotel_name: str
    price_per_night: float
    currency: str = "INR"
    room_type: Optional[str] = "Standard"
    discount_percentage: Optional[float] = 0.0
    source_url: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    confidence_score: float = Field(default=0.95, ge=0.0, le=1.0)
    validation_notes: Optional[str] = "Verified from live DOM"