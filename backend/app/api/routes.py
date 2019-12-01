from flask import request, jsonify
from lib.services import WebService
from app.api import bp


service = WebService()

@bp.route('/api/load_test', methods=['POST'])
def test_endpoint():
    data = request.json
    total_time, request_dict = entrypoint(data["url"], int(data["requests"]), int(data["concurrency"]))
    results = Results(total_time, request_dict)
    response = {
        "objects": request_dict,
        "total_time": total_time,
        "slowest": results.slowest(),
        "fastest": results.fastest(),
        "average": results.average_time(),
        "requests_per_min": results.requests_per_min(),
        "requests_per_sec": results.requests_per_sec()
    }
    return jsonify(response)


@bp.route('/api/endpoints', methods=['GET', 'POST'])
def load_services():
    data = request.json
    url = data['body']
    response = {
        'endpoints': service(url)
    }
    return jsonify(response)