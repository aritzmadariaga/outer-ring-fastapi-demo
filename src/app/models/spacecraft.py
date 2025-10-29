from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from src.app.db.base import Base

class Spacecraft(Base):
    __tablename__ = "spacecraft"

    id = Column(Integer, primary_key=True, index=True)
    registry_code = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    manufacturer = Column(String(255))
    crew_capacity = Column(Integer)
    max_delta_v = Column(Integer)
    operational = Column(Boolean, default=True)
    first_flight_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
