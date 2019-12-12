import pytest
import asyncio
from app import create_app, db
from configs import TestingConfig


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


