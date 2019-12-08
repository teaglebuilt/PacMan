import pytest
import asyncio
from app import create_app
from configs import TestingConfig


TEST_DB = 'sqlite:///:memory:'

@pytest.fixture
def app():
    return create_app(TestingConfig)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    from app import db
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()


@pytest.fixture(scope='session')
def loop():
    return asyncio.get_event_loop()


# @pytest.fixture
# def module_client(scope='module'):
#     Config.SQLALCHEMY_DATABASE_URI = TEST_DB
#     Config.TESTING = True
#     app = create_app(Config)
#     test_client = app.test_client()
#     ctx = app.app_context()
#     ctx.push()

#     yield test_client
#     ctx.pop()

