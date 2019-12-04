import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from sqlalchemy_utils import URLType
from app import create_app, db, cli
from configs import DevelopmentConfig

app = create_app(DevelopmentConfig)

    

if __name__ == '__main__':
    manager.run()