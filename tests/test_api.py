from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

#Que otros test puedo hacer? Puedo hacer un test de prediccion? hazlo
def test_prediction():
    payload = {
        "gender": "Male",
        "age": 30, 
        "annual_income_k": 60,
        "spending_score": 70
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "probability" in response.json()
                                     