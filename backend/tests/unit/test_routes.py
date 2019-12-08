from tests import conftest
import json


def test_endpoints(client):
    response = client.get('/api/endpoints', json={
        "body": "https://petstore.swagger.io/v2/swagger.json"
    })
    assert (response.status_code == 200)


def test_load_test(client):
    response = client.post('/api/load_test', json={
        "url": "https://petstore.swagger.io/v2/swagger.json",
        "requests": "100",
        "concurrency": "10"
    })
    assert (response.status_code == 200)