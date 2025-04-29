import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config.settings


def test_config_settings():
    assert config.settings.APP_NAME == "TestApp"
    assert config.settings.VERSION == "0.1.0"
    assert config.settings.DEBUG is True
