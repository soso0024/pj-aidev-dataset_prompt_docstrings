import pytest
from config.settings import APP_NAME, VERSION, DEBUG

def test_app_name():
    assert APP_NAME == "TestApp"

def test_version():
    assert VERSION == "0.1.0"

def test_debug():
    assert DEBUG is True
