from app import create_app, cli, db
from app.models import Service, Result
from configs import DevelopmentConfig
from prometheus_client import make_wsgi_app


app = create_app(DevelopmentConfig)
cli.register(app, db)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Service': Service, 'Result': Result}