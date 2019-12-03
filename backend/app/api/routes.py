from flask import request, jsonify
from lib.services import WebService
from app.handlers.queue import entrypoint
from app.handlers.calculate import Results
from app.api import bp
from app.models import Service, Result
from app import db


service_lib = WebService()

@bp.route('/api/load_test', methods=['POST'])
def test_endpoint():
    data = request.json
    time, request_dict = entrypoint(data["url"], int(data["requests"]), int(data["concurrency"]))
    results = Results(time, request_dict)
    response = {
        "objects": request_dict,
        "total_time": total_time,
        "slowest": results.slowest(),
        "fastest": results.fastest(),
        "average": results.average_time(),
        "requests_per_min": results.requests_per_min(),
        "requests_per_sec": results.requests_per_sec()
    }
    obj = Result(url=data["url"], total_time=time, result_all=response)
    db.session.add(obj)
    db.session.commit()
    return jsonify(response)


@bp.route('/api/endpoints', methods=['GET', 'POST'])
def load_services():
    data = request.json
    url = data['body']
    service_data = service_lib(url)
    try:
        service = Service(
            url=data['body']
        )
        db.session.add(service)
        db.session.commit()
    except:
        print("error")
        
    response = {
        'endpoints': service_data
    }
    return jsonify(response)