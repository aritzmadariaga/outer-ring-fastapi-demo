from sqlalchemy.orm import Session
from src.app.db.session import SessionLocal
from src.app.models.spacecraft import Spacecraft

def seed_data(db: Session) -> None:
    # Create sample spacecraft
    if db.query(Spacecraft).count() == 0:
        spacecrafts = [
            Spacecraft(registry_code="NCC-1701", name="USS Enterprise", manufacturer="Starfleet", crew_capacity=430, max_delta_v=4000, operational=True),
            Spacecraft(registry_code="NCC-74656", name="USS Voyager", manufacturer="Starfleet", crew_capacity=150, max_delta_v=9975, operational=True),
            Spacecraft(registry_code="DS1-001", name="Deep Space One", manufacturer="NASA", crew_capacity=0, max_delta_v=10000, operational=False),
        ]
        db.add_all(spacecrafts)
        db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    seed_data(db)
    db.close()
