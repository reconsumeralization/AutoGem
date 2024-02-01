from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_tool_endpoint_success():
    # Assuming the tool endpoint expects a GET request
    response = client.get("/tool")
    assert response.status_code == 200
    # Add more assertions based on the expected JSON structure

def test_tool_endpoint_failure():
    # Assuming there's a way to simulate a failure, like an invalid parameter
    response = client.get("/tool?invalid_param=1")
    assert response.status_code == 400
    # Add more assertions based on the expected error response
