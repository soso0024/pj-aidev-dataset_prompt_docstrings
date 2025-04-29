import pytest
from config.settings import APP_NAME, VERSION, DEBUG


def test_config_settings():
    assert APP_NAME == "TestApp"
    assert VERSION == "0.1.0"
    assert DEBUG is True
