from app import create_app
from configs import DevelopmentConfig
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app


application = create_app(DevelopmentConfig)


app_dispatch = DispatcherMiddleware(application, {
    '/metrics': make_wsgi_app()
})

