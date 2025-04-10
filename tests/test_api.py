from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_password():
    response = client.post("/password/testservice", json={"password": "mypassword"})
    assert response.status_code == 200
    assert response.json()["service_name"] == "testservice"

    get_response = client.get("/password/testservice")
    assert get_response.status_code == 200
    assert get_response.json()["password"] == "mypassword"

def test_search_password():
    response = client.get("/password/", params={"service_name": "test"})
    assert response.status_code == 200
    assert any(p["service_name"] == "testservice" for p in response.json())
