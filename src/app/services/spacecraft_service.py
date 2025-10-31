from sqlalchemy.orm import Session
from app.repositories.spacecraft_repository import SpacecraftRepository
from app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate


class SpacecraftService:
    """
    Service layer for spacecraft business logic.

    This class provides methods to create, retrieve, list, update, and delete spacecrafts
    using the SpacecraftRepository. It abstracts the repository and can contain additional
    business rules or validations in the future.
    """

    def __init__(self, db: Session):
        """
        Initialize the SpacecraftService.

        Args:
            db (Session): SQLAlchemy database session.
        """
        self.repository = SpacecraftRepository(db)

    from app.models.spacecraft import Spacecraft

    def create_spacecraft(self, spacecraft: SpacecraftCreate) -> "Spacecraft":
        """
        Create a new spacecraft.

        Args:
            spacecraft (SpacecraftCreate): The spacecraft data to create.

        Returns:
            Spacecraft: The created spacecraft ORM object.
        """
        return self.repository.create(spacecraft)

    def get_spacecraft(self, spacecraft_id: int) -> "Spacecraft | None":
        """
        Retrieve a spacecraft by its ID.

        Args:
            spacecraft_id (int): The ID of the spacecraft to retrieve.

        Returns:
            Spacecraft | None: The spacecraft ORM object or None if not found.
        """
        return self.repository.get(spacecraft_id)

    def get_all_spacecrafts(
        self, skip: int = 0, limit: int = 100
    ) -> list["Spacecraft"]:
        """
        List all spacecrafts with pagination.

        Args:
            skip (int): Number of records to skip (default: 0).
            limit (int): Maximum number of records to return (default: 100).

        Returns:
            list[Spacecraft]: List of spacecraft ORM objects.
        """
        return self.repository.get_all(skip, limit)

    def update_spacecraft(
        self, spacecraft_id: int, spacecraft: SpacecraftUpdate
    ) -> "Spacecraft | None":
        """
        Update an existing spacecraft by its ID.

        Args:
            spacecraft_id (int): The ID of the spacecraft to update.
            spacecraft (SpacecraftUpdate): The updated spacecraft data.

        Returns:
            Spacecraft | None: The updated spacecraft ORM object or None if not found.
        """
        return self.repository.update(spacecraft_id, spacecraft)

    def delete_spacecraft(self, spacecraft_id: int) -> "Spacecraft | None":
        """
        Delete a spacecraft by its ID.

        Args:
            spacecraft_id (int): The ID of the spacecraft to delete.

        Returns:
            Spacecraft | None: The deleted spacecraft ORM object or None if not found.
        """
        return self.repository.delete(spacecraft_id)
