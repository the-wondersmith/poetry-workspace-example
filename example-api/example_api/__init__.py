"""A super simple example of using FastAPI in a "workspace"-style repository
pattern."""

# Future Imports
from __future__ import annotations

__pkg_name__ = "example_api"
__version__ = "0.1.0"  # x-release-please-version

# Imports From Package Sub-Modules
from . import endpoints
from .core import app
