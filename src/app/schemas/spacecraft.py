from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SpacecraftBase(BaseModel):
    """
    Base schema for spacecraft data.
    """
    registry_code: str  #: :no-index:
    name: str  #: :no-index:
    manufacturer: Optional[str] = None  #: :no-index:
    crew_capacity: Optional[int] = None  #: :no-index:
    max_delta_v: Optional[int] = None  #: :no-index:
    operational: bool = True  #: :no-index:
    first_flight_at: Optional[datetime] = None  #: :no-index:

class SpacecraftCreate(SpacecraftBase):
    """
    Schema for creating a new spacecraft.
    Inherits all fields from SpacecraftBase.
    """
    pass

class SpacecraftUpdate(SpacecraftBase):
    """
    Schema for updating an existing spacecraft.
    Inherits all fields from SpacecraftBase.
    """
    pass

class SpacecraftInDB(SpacecraftBase):
    """
    Schema representing a spacecraft as stored in the database.
    """
    id: int  #: :no-index:
    created_at: datetime  #: :no-index:
    updated_at: datetime  #: :no-index:

    class Config:
        from_attributes = True
