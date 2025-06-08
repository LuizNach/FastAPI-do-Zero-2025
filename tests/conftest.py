import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi_zero.app import app
from fastapi_zero.models import table_registry


@pytest.fixture
def client() -> TestClient:
    # Arrange
    return TestClient(app=app)


@pytest.fixture
def session():
    # Setup/Arrange
    engine = create_engine(url='sqlite:///:memory')
    table_registry.metadata.create_all(bind=engine)

    with Session(engine) as session:
        yield session

    # Teardown
    table_registry.metadata.drop_all(bind=engine)
