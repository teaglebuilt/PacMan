from app import create_app
from configs import DevelopmentConfig
from prometheus_client import make_wsgi_app


app = create_app(DevelopmentConfig)




