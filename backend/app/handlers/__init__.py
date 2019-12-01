from flask import Blueprint


bp = Blueprint('handlers', __name__)


from app.handlers import calculate, queue