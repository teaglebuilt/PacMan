from configs import Config
from flask import Flask
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__, static_folder=None)
    app.config.from_object(config_class)
    CORS(app)
    from app.api import bp as api
    app.register_blueprint(api)
    from app.handlers import bp as handlers
    app.register_blueprint(handlers)
    return app
    