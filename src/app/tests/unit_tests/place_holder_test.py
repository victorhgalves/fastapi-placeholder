from typing import Optional
from src.main import app
from fastapi.testclient import TestClient
from src.app.middlewares import authentication

client = TestClient(app)

def test_should_return_status_success():
    response = client.get('/placeholder/info')
    assert response.status_code == 200

def test_should_return_values():
    response = client.get('/placeholder/info')
    assert len(response.content) > 0

def test_should_return_title_in_request():
    response = client.get('/placeholder/info')
    assert "title" in response.json()[0]

def test_should_return_id_in_request():
    response = client.get('/placeholder/info')
    assert "id" in response.json()[0]

def test_should_return_id_in_request_with_int_format():
    response = client.get('/placeholder/info')
    assert isinstance(response.json()[0]['id'], int)

def test_should_return_title_in_request_with_string_format():
    response = client.get('/placeholder/info')
    assert isinstance(response.json()[0]['title'], str)