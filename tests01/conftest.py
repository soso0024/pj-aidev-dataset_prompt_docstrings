import pytest
import sys
import os

# Add the project root directory to the Python path
# This ensures imports work correctly in test modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
