from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    print(response)
    assert response.status_code == 200
    print(response.headers)
    assert "text/html" in  response.headers['content-type']

def test_get_home():
    response = client.post("/")
    print(response)
    assert response.status_code == 200
    print(response.headers)
    assert "application/json" in  response.headers['content-type']
   
    