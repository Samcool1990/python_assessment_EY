from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def addition_payload():
    return {
        "batchcid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }

def test_addition_success(addition_payload):
    response = client.post("/api/v1/add", json=addition_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["batchcid"] == addition_payload["batchcid"]
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"

def test_addition_invalid_payload():
    response = client.post("/api/v1/add", json={"batchcid": "id0101", "payload": [[1, "a"], [3, 4]]})
    assert response.status_code == 422  # Unprocessable Entity due to invalid input

def test_addition_empty_payload():
    response = client.post("/api/v1/add", json={"batchcid": "id0101", "payload": []})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == []
    assert data["status"] == "complete"
