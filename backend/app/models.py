from app import db
from sqlalchemy_utils import URLType



class Service(db.Model):
    uri = db.Column(URLType, nullable=False, unique=True)

    def __repr__(self):
        return f"Service: {}".format(self.uri)