from datetime import datetime, timedelta
from flask import request, jsonify, make_response, session
from .exceptions import PasswordMatchError
from lib.services import WebService
from app.handlers.queue import entrypoint
from app.handlers.calculate import Results
from app.decorators.debugger import Debugger
from app.models import Service, Result
from app.api import bp
from app import db
import jwt


service_lib = WebService()
Debugger.enabled = True


@bp.route('/api/load_test', methods=['POST'])
def test_endpoint():
    data = request.json
    time, request_dict = entrypoint(data["url"], int(data["requests"]), int(data["concurrency"]))
    results = Results(time, request_dict)
    response = {
        "objects": request_dict,
        "total_time": time,
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
    print(request.__dict__)
    service_data = service_lib(url)
    try:
        service = Service(
            url=data['body']
        )
        db.session.add(service)
        db.session.commit()
    except Exception as e:
        print(f"error {e}")
        
    response = {
        'endpoints': service_data
    }
    return jsonify(response)