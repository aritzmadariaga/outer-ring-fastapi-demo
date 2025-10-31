import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from typing import Generator, AsyncGenerator
from sqlalchemy.orm import Session
from app.db.base import Base
from app.main import app
from app.db.dependencies import get_db
from httpx import AsyncClient

# Build DB URL from environment so CI can control the host/port via env vars.
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "outer_ring")

# Allow forcing SQLite in-memory for pure unit runs (useful in CI or local dev)
USE_SQLITE = os.getenv("TEST_SQLITE", "0") == "1"

if USE_SQLITE:
    SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///:memory:"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Try to create tables; if the DB is not reachable, fall back to SQLite in-memory.
try:
    # attempt a quick connection to ensure DB reachable
    conn = engine.connect()
    conn.close()
    Base.metadata.create_all(bind=engine)
except OperationalError:
    # Fallback: use sqlite memory DB for tests to avoid external dependency
    SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///:memory:"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal.configure(bind=engine)
    Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db_session() -> Generator[Session, None, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
async def client(db_session: Session) -> AsyncGenerator[AsyncClient, None]:
    def override_get_db() -> Generator[Session, None, None]:
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
