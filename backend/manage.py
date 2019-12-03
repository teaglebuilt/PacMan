import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from sqlalchemy_utils import URLType
from app import create_app, db
from configs import DevelopmentConfig

app = create_app(DevelopmentConfig)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()