from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def valid_request_body():
    return {
        "bathcid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }

def test_addition(valid_request_body):
    response = client.post("/add", json=valid_request_body)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["bathcid"] == valid_request_body["bathcid"]
    assert json_response["response"] == [3, 7]
    assert json_response["status"] == "complete"
    assert "started_at" in json_response
    assert "completed_at" in json_response

def test_addition_invalid_payload():
    response = client.post("/add", json={"bathcid": "id0101", "payload": "invalid"})
    assert response.status_code == 422  # Unprocessable Entity

def test_addition_empty_payload():
    response = client.post("/add", json={"bathcid": "id0101", "payload": []})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["response"] == []
