import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import patch, MagicMock
import main
from config.settings import APP_NAME, VERSION


@patch("builtins.print")
def test_run_demo_prints_version(mock_print):
    # Just test that the version is printed correctly
    with patch("data.generator.generate_users", return_value=[]):
        with patch("data.generator.generate_orders", return_value=[]):
            main.run_demo()
            mock_print.assert_any_call(f"{APP_NAME} v{VERSION} starting...")
            mock_print.assert_any_call("Demo complete.")


def test_main_entry_point():
    # Very simple test to just make sure the module imports correctly
    assert hasattr(main, "run_demo")
    # And has the expected behavior of running when executed as main
    with open(main.__file__, "r") as f:
        content = f.read()
        assert 'if __name__ == "__main__":' in content
        assert "run_demo()" in content
