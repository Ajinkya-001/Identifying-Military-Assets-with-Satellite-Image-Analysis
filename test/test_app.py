from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 404  # root isn’t defined

def test_inference_upload():
    with open("tests/sample.jpg", "rb") as f:
        response = client.post("/detect", files={"file": ("sample.jpg", f, "image/jpeg")})
    assert response.status_code == 200
