from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.app.services.spacecraft_service import SpacecraftService
from src.app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate, SpacecraftInDB
from src.app.db.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=SpacecraftInDB)
def create_spacecraft(spacecraft: SpacecraftCreate, db: Session = Depends(get_db)):
    service = SpacecraftService(db)
    return service.create_spacecraft(spacecraft)

@router.get("/{spacecraft_id}", response_model=SpacecraftInDB)
def read_spacecraft(spacecraft_id: int, db: Session = Depends(get_db)):
    service = SpacecraftService(db)
    db_spacecraft = service.get_spacecraft(spacecraft_id)
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail="Spacecraft not found")
    return db_spacecraft

@router.get("/", response_model=list[SpacecraftInDB])
def read_spacecrafts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = SpacecraftService(db)
    return service.get_all_spacecrafts(skip, limit)

@router.put("/{spacecraft_id}", response_model=SpacecraftInDB)
def update_spacecraft(spacecraft_id: int, spacecraft: SpacecraftUpdate, db: Session = Depends(get_db)):
    service = SpacecraftService(db)
    db_spacecraft = service.update_spacecraft(spacecraft_id, spacecraft)
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail="Spacecraft not found")
    return db_spacecraft

@router.delete("/{spacecraft_id}", response_model=SpacecraftInDB)
def delete_spacecraft(spacecraft_id: int, db: Session = Depends(get_db)):
    service = SpacecraftService(db)
    db_spacecraft = service.delete_spacecraft(spacecraft_id)
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail="Spacecraft not found")
    return db_spacecraft
