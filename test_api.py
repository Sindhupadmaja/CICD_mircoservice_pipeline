from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_create_order():
    client = app.test_client()
    response = client.post("/orders", json={"item": "keyboard"})
    assert response.status_code == 201
