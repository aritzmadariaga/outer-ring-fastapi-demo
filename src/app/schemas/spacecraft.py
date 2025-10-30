from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


class SpacecraftBase(BaseModel):
    """
    Base schema for spacecraft data.
    """
    registry_code: str = Field(..., description="Unique registry code for the spacecraft.", json_schema_extra={"example": "OR-001"})
    name: str = Field(..., description="Name of the spacecraft.", json_schema_extra={"example": "Outer Explorer"})
    manufacturer: Optional[str] = Field(None, description="Manufacturer of the spacecraft.", json_schema_extra={"example": "Deusto"})
    crew_capacity: Optional[int] = Field(None, description="Maximum crew capacity.", json_schema_extra={"example": 5})
    max_delta_v: Optional[int] = Field(None, description="Maximum delta-v (m/s).", json_schema_extra={"example": 12000})
    operational: bool = Field(True, description="Whether the spacecraft is operational.", json_schema_extra={"example": True})
    first_flight_at: Optional[datetime] = Field(None, description="Date of first flight.", json_schema_extra={"example": "2025-10-30T00:00:00Z"})

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

    model_config = ConfigDict(from_attributes=True)
