from tests import conftest
import pytest
import asyncio
import json


def test_endpoints(module_client, module_db):
    response = module_client.get('/api/endpoints', json={
        "body": "https://petstore.swagger.io/v2/swagger.json"
    })
    assert (response.status_code == 200)


def test_load_test(module_client, module_db):
    response = module_client.post('/api/load_test', json={
        "url": "https://petstore.swagger.io/v2/1",
        "requests": "10",
        "concurrency": "2"
    })
    data = response.get_json()
    assert (response.status_code == 200)
    assert data['average'] != None

    


