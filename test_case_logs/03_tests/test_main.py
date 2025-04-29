import pytest
from unittest.mock import patch, MagicMock


def test_app_name_version():
    with patch("config.settings.APP_NAME", "TestApp"):
        with patch("config.settings.VERSION", "0.1.0"):
            with patch("builtins.print") as mock_print:
                # Import the module inside the test with patches applied
                from main import run_demo

                # Patch all functions to do nothing and avoid side effects
                with patch("data.generator.generate_users", return_value=[]):
                    with patch("data.generator.generate_orders", return_value=[]):
                        # Run the function with empty lists so it finishes quickly
                        run_demo()

                        # Test only that the app name and version were printed
                        mock_print.assert_any_call("TestApp v0.1.0 starting...")
                        mock_print.assert_any_call("Demo complete.")
