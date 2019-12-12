from app import db
from sqlalchemy_utils import URLType
from sqlalchemy.dialects.postgresql import JSON


class Service(db.Model):
    
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(URLType, nullable=False, unique=True)

    def __repr__(self):
        return f"Service: {self.url}"


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    total_time = db.Column(db.Integer())
    result_all = db.Column(JSON)

    def __init__(self, url, total_time, result_all):
        self.url = url
        self.result_all = result_all
        self.total_time = total_time

    def __repr__(self):
        return '<Result for: {} with total: {}>'.format(self.url, self.total_time)