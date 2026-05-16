from fastapi.testclient import TestClient
import pytest

from src.app import app, reset_activities


@pytest.fixture(autouse=True)
def reset_activity_data():
    reset_activities()
    yield
    reset_activities()


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client