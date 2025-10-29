from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SpacecraftBase(BaseModel):
    registry_code: str
    name: str
    manufacturer: Optional[str] = None
    crew_capacity: Optional[int] = None
    max_delta_v: Optional[int] = None
    operational: bool = True
    first_flight_at: Optional[datetime] = None

class SpacecraftCreate(SpacecraftBase):
    pass

class SpacecraftUpdate(SpacecraftBase):
    pass

class SpacecraftInDB(SpacecraftBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
