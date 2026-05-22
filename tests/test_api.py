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

def test_prediction():
    payload = {
        "gender": "Male",
        "age": 30,      
        "annual_income_k": 60,
        "spending_score": 50
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_segment" in response.json()
    assert response.json()["predicted_segment"] in ["Segment 1", "Segment 2", "Segment 3", "Segment 4"]
    #falta?
    assert "prediction_time_seconds" in response.json()
    assert response.json()["prediction_time_seconds"] < 1.0



    