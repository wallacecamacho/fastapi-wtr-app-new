import json

import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    response = client.get('/api')
    assert response.status_code == 200

def test_read_tickers():
    response = client.get('/api/tickers')
    assert response.status_code == 200

def test_read_tickers_goog():
    response = client.get('/api/tickers/GOOG')
    assert response.status_code == 200

def test_read_ping_ping():
    response = client.get('/api/ping/poing')
    assert response.status_code == 404
