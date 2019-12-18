import pytest
import asyncio
from app import create_app, db
from configs import TestingConfig



@pytest.fixture(scope='module')
def module_client():
    flask_app = create_app(TestingConfig)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture(scope='module')
def module_db():
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


