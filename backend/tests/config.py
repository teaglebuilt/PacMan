import pytest
from configs import Config


TEST_DATABASE_URI = 'sqlite:///:memory:'


@pytest.fixture(scope='session')
def app(request):
    Config.SQLALCHEMY_DATABASE_URI = TEST_DATABASE_URI
    Config.TESTING = True
    app = create_app(Config)
    print(dir(app))
    return app

    

