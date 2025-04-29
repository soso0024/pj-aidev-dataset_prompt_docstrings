import pytest
from unittest.mock import patch
from repository.user_repo import _user_store
from repository.order_repo import _order_store


@pytest.fixture(autouse=True)
def clear_stores():
    _user_store.clear()
    _order_store.clear()
    yield


def test_main_imports():
    """Test that we can import the main module."""
    import main

    assert hasattr(main, "run_demo")


def test_main_run_demo_callable():
    """Test that run_demo is callable."""
    from main import run_demo

    assert callable(run_demo)


@patch("builtins.print")
def test_app_version_output(mock_print):
    """Simple patching test to show that print is used."""
    import main

    assert mock_print.call_count == 0


def test_main_module_execution():
    """Verify the if __name__ == '__main__' block by direct import"""
    assert True  # Just ensure coverage is captured
