from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from app.db.base import Base


class Spacecraft(Base):
    """
    SQLAlchemy ORM model for the spacecraft table.
    """

    __tablename__ = "spacecraft"

    id = Column(Integer, primary_key=True, index=True)  #: :no-index:
    registry_code = Column(
        String(255), unique=True, index=True, nullable=False
    )  #: :no-index:
    name = Column(String(255), nullable=False)  #: :no-index:
    manufacturer = Column(String(255))  #: :no-index:
    crew_capacity = Column(Integer)  #: :no-index:
    max_delta_v = Column(Integer)  #: :no-index:
    operational = Column(Boolean, default=True)  #: :no-index:
    first_flight_at = Column(DateTime, nullable=True)  #: :no-index:
    created_at = Column(DateTime, server_default=func.now())  #: :no-index:
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )  #: :no-index:
