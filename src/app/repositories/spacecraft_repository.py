from sqlalchemy.orm import Session
from app.models.spacecraft import Spacecraft
from app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate


class SpacecraftRepository:
    """
    Repository for database operations related to spacecraft.

    Provides methods to create, retrieve, list, update, and delete spacecraft records
    in the database using SQLAlchemy ORM.
    """

    def __init__(self, db: Session):
        """
        Initialize the SpacecraftRepository.

        Args:
            db (Session): SQLAlchemy database session.
        """
        self.db = db

    def create(self, spacecraft: SpacecraftCreate) -> Spacecraft:
        """
        Create a new spacecraft record in the database.

        Args:
            spacecraft (SpacecraftCreate): The spacecraft data to create.

        Returns:
            Spacecraft: The created spacecraft ORM object.
        """
        db_spacecraft = Spacecraft(**spacecraft.model_dump())
        self.db.add(db_spacecraft)
        self.db.commit()
        self.db.refresh(db_spacecraft)
        return db_spacecraft

    def get(self, spacecraft_id: int) -> Spacecraft | None:
        """
        Retrieve a spacecraft by its ID.

        Args:
            spacecraft_id (int): The ID of the spacecraft to retrieve.

        Returns:
            Spacecraft | None: The spacecraft ORM object or None if not found.
        """
        return self.db.query(Spacecraft).filter(Spacecraft.id == spacecraft_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Spacecraft]:
        """
        List all spacecrafts with pagination.

        Args:
            skip (int): Number of records to skip (default: 0).
            limit (int): Maximum number of records to return (default: 100).

        Returns:
            list[Spacecraft]: List of spacecraft ORM objects.
        """
        return self.db.query(Spacecraft).offset(skip).limit(limit).all()

    def update(
        self, spacecraft_id: int, spacecraft: SpacecraftUpdate
    ) -> Spacecraft | None:
        """
        Update an existing spacecraft record by its ID.

        Args:
            spacecraft_id (int): The ID of the spacecraft to update.
            spacecraft (SpacecraftUpdate): The updated spacecraft data.

        Returns:
            Spacecraft | None: The updated spacecraft ORM object or None if not found.
        """
        db_spacecraft = self.get(spacecraft_id)
        if db_spacecraft:
            update_data = spacecraft.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_spacecraft, key, value)
            self.db.commit()
            self.db.refresh(db_spacecraft)
        return db_spacecraft

    def delete(self, spacecraft_id: int) -> Spacecraft | None:
        """
        Delete a spacecraft record by its ID.

        Args:
            spacecraft_id (int): The ID of the spacecraft to delete.

        Returns:
            Spacecraft | None: The deleted spacecraft ORM object or None if not found.
        """
        db_spacecraft = self.get(spacecraft_id)
        if db_spacecraft:
            self.db.delete(db_spacecraft)
            self.db.commit()
        return db_spacecraft
