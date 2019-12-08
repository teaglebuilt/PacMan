import pytest
from app.models import Service, Result
from tests import conftest



def test_service(db):
    service = Service(
        url='https://petstore.swagger.io/v2/swagger.json'
    )
    assert (service.url == "https://petstore.swagger.io/v2/swagger.json")
    assert (str(service) == "Service: https://petstore.swagger.io/v2/swagger.json")


# def test_results(db):
#     response = {
#         "objects": request_dict,
#         "total_time": time,
#         "slowest": results.slowest(),
#         "fastest": results.fastest(),
#         "average": results.average_time(),
#         "requests_per_min": results.requests_per_min(),
#         "requests_per_sec": results.requests_per_sec()
#     }
#     results = Result(
#         url = 'https://petstore.swagger.io/v2/swagger.json',
#         total_time="",
#         results_all=""
#     )