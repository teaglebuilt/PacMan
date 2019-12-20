from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify
from .exceptions import PasswordMatchError
from lib.services import WebService
from app.decorators.auth import check_for_token
from app.handlers.queue import entrypoint
from app.handlers.calculate import Results
from app.decorators.debugger import Debugger
from app.models import Service, Result
from app.api import bp
from app import db
import jwt


service_lib = WebService()
Debugger.enabled = True


@check_for_token
@bp.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    username = data['username']
    password = data['password']
    confirm_pw = data['confirm_password']
    if password == confirm_pw:
        "TODO create user w/ User model <<<<<"
        return jsonify({'message': 'Welcome {}! You are now registered and redirected to login with your account.'})
    elif password != confirm_pw:
        return "error"
    else:
        raise Exception(request.json)
    

@check_for_token
def login():
    if request.form['username'] and request.form['password'] == 'password':
        session['logged_in'] = True
    token = jwt.encode({
        'user': request.form['username'],
        'exp': datetime.datetime.now() + timedelta(seconds=60)
    }, app.config['SECRET_KEY'])
    

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
    except:
        print("error")
        
    response = {
        'endpoints': service_data
    }
    return jsonify(response)