"""Configuration and fixtures for pytest."""

import pytest
import sys
from io import StringIO
from unittest.mock import patch
from src.todo_app.services.todo_service import TodoService


@pytest.fixture
def todo_service():
    """Create a fresh TodoService instance for each test."""
    return TodoService()


@pytest.fixture
def captured_output():
    """Capture stdout for testing CLI output."""
    old_stdout = sys.stdout
    captured = StringIO()
    sys.stdout = captured
    yield captured
    sys.stdout = old_stdout


@pytest.fixture
def mock_args():
    """Create a mock args object for CLI testing."""
    class Args:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
    return Args