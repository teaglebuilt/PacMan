from app import create_app, cli, db
from app.models import Service, Result
from configs import DevelopmentConfig
from dotenv import load_dotenv
import os
load_dotenv()


app = create_app(os.getenv('APP_SETTINGS'))
cli.register(app, db)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Service': Service, 'Result': Result}