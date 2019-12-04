from app.models import Service, Result
from app import db



def register(app, db):
    @app.cli.group()
    def db_migrate():
        pass

    @db_migrate.command
    def init():
        print(db)
    
    @db_migrate.command()
    def create_tables():
        db.create_all()
        print('Database created!')