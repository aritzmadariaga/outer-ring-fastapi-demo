from sqlalchemy.orm import Session
from src.app.repositories.spacecraft_repository import SpacecraftRepository
from src.app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate

class SpacecraftService:
    def __init__(self, db: Session):
        self.repository = SpacecraftRepository(db)

    def create_spacecraft(self, spacecraft: SpacecraftCreate):
        return self.repository.create(spacecraft)

    def get_spacecraft(self, spacecraft_id: int):
        return self.repository.get(spacecraft_id)

    def get_all_spacecrafts(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all(skip, limit)

    def update_spacecraft(self, spacecraft_id: int, spacecraft: SpacecraftUpdate):
        return self.repository.update(spacecraft_id, spacecraft)

    def delete_spacecraft(self, spacecraft_id: int):
        return self.repository.delete(spacecraft_id)
