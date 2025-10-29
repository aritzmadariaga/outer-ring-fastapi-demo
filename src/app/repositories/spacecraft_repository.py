from sqlalchemy.orm import Session
from src.app.models.spacecraft import Spacecraft
from src.app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate

class SpacecraftRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, spacecraft: SpacecraftCreate) -> Spacecraft:
        db_spacecraft = Spacecraft(**spacecraft.model_dump())
        self.db.add(db_spacecraft)
        self.db.commit()
        self.db.refresh(db_spacecraft)
        return db_spacecraft

    def get(self, spacecraft_id: int) -> Spacecraft | None:
        return self.db.query(Spacecraft).filter(Spacecraft.id == spacecraft_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Spacecraft]:
        return self.db.query(Spacecraft).offset(skip).limit(limit).all()

    def update(self, spacecraft_id: int, spacecraft: SpacecraftUpdate) -> Spacecraft | None:
        db_spacecraft = self.get(spacecraft_id)
        if db_spacecraft:
            update_data = spacecraft.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_spacecraft, key, value)
            self.db.commit()
            self.db.refresh(db_spacecraft)
        return db_spacecraft

    def delete(self, spacecraft_id: int) -> Spacecraft | None:
        db_spacecraft = self.get(spacecraft_id)
        if db_spacecraft:
            self.db.delete(db_spacecraft)
            self.db.commit()
        return db_spacecraft
