import pytest


@pytest.fixture
def begin_message():
    print("Test begin")
    return "Test end"
