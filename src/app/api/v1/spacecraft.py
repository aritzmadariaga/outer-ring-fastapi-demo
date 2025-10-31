"""
API endpoints for managing spacecraft resources.

This module provides CRUD operations for spacecraft, including creation, retrieval,
listing, updating, and deletion. All endpoints require a database session and use
the SpacecraftService for business logic.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.spacecraft_service import SpacecraftService
from app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate, SpacecraftInDB
from app.db.dependencies import get_db

router = APIRouter()


@router.post(
    "/",
    response_model=SpacecraftInDB,
    tags=["Spacecraft"],
    summary="Create a new spacecraft",
    description="Creates a new spacecraft in the database with the provided details.",
    responses={
        201: {"description": "Spacecraft created successfully."},
        400: {"description": "Invalid input."},
        409: {"description": "Spacecraft with this registry code already exists."},
    },
)
def create_spacecraft(spacecraft: SpacecraftCreate, db: Session = Depends(get_db)):
    """
    Create a new spacecraft.

    Args:
        spacecraft (SpacecraftCreate): The spacecraft data to create.
        db (Session): SQLAlchemy database session (injected).

    Returns:
        SpacecraftInDB: The created spacecraft with database fields.
    """
    service = SpacecraftService(db)
    return service.create_spacecraft(spacecraft)


@router.get(
    "/{spacecraft_id}",
    response_model=SpacecraftInDB,
    tags=["Spacecraft"],
    summary="Get a spacecraft by ID",
    description="Retrieve a spacecraft by its unique database ID.",
    responses={
        200: {"description": "Spacecraft found and returned."},
        404: {"description": "Spacecraft not found."},
    },
)
def read_spacecraft(spacecraft_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a spacecraft by its ID.

    Args:
        spacecraft_id (int): The ID of the spacecraft to retrieve.
        db (Session): SQLAlchemy database session (injected).

    Returns:
        SpacecraftInDB: The requested spacecraft.

    Raises:
        HTTPException: If the spacecraft is not found (404).
    """
    service = SpacecraftService(db)
    db_spacecraft = service.get_spacecraft(spacecraft_id)
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail="Spacecraft not found")
    return db_spacecraft


@router.get(
    "/",
    response_model=list[SpacecraftInDB],
    tags=["Spacecraft"],
    summary="List all spacecrafts",
    description="List all spacecrafts with pagination support.",
    responses={200: {"description": "List of spacecrafts returned."}},
)
def read_spacecrafts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    List all spacecrafts with pagination.

    Args:
        skip (int): Number of records to skip (default: 0).
        limit (int): Maximum number of records to return (default: 100).
        db (Session): SQLAlchemy database session (injected).

    Returns:
        list[SpacecraftInDB]: List of spacecrafts.
    """
    service = SpacecraftService(db)
    return service.get_all_spacecrafts(skip, limit)


@router.put(
    "/{spacecraft_id}",
    response_model=SpacecraftInDB,
    tags=["Spacecraft"],
    summary="Update a spacecraft",
    description="Update an existing spacecraft by its ID.",
    responses={
        200: {"description": "Spacecraft updated successfully."},
        404: {"description": "Spacecraft not found."},
        400: {"description": "Invalid input."},
    },
)
def update_spacecraft(
    spacecraft_id: int, spacecraft: SpacecraftUpdate, db: Session = Depends(get_db)
):
    """
    Update an existing spacecraft by its ID.

    Args:
        spacecraft_id (int): The ID of the spacecraft to update.
        spacecraft (SpacecraftUpdate): The updated spacecraft data.
        db (Session): SQLAlchemy database session (injected).

    Returns:
        SpacecraftInDB: The updated spacecraft.

    Raises:
        HTTPException: If the spacecraft is not found (404).
    """
    service = SpacecraftService(db)
    db_spacecraft = service.update_spacecraft(spacecraft_id, spacecraft)
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail="Spacecraft not found")
    return db_spacecraft


@router.delete(
    "/{spacecraft_id}",
    response_model=SpacecraftInDB,
    tags=["Spacecraft"],
    summary="Delete a spacecraft",
    description="Delete a spacecraft by its ID.",
    responses={
        200: {"description": "Spacecraft deleted successfully."},
        404: {"description": "Spacecraft not found."},
    },
)
def delete_spacecraft(spacecraft_id: int, db: Session = Depends(get_db)):
    """
    Delete a spacecraft by its ID.

    Args:
        spacecraft_id (int): The ID of the spacecraft to delete.
        db (Session): SQLAlchemy database session (injected).

    Returns:
        SpacecraftInDB: The deleted spacecraft.

    Raises:
        HTTPException: If the spacecraft is not found (404).
    """
    service = SpacecraftService(db)
    db_spacecraft = service.delete_spacecraft(spacecraft_id)
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail="Spacecraft not found")
    return db_spacecraft
