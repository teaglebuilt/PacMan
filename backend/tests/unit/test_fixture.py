import pytest
from tests import conftest


def test_app_creates(app):
    assert app


async def test_event_loop(event_loop):
    expected = 'This should fail!'
    assert expected == event_loop.run_until_complete(say('Hello!', 0))