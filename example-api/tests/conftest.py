"""PyTest configuration & fixtures for the example's unit test suite."""

# Future Imports
from __future__ import annotations

# Standard Library Imports
from typing import Generator

# Third-Party Imports
import pytest
from httpx import AsyncClient

# Package-Level Imports
from example_api.core import app

__all__ = tuple()


# <editor-fold desc="# Auto-used, Session-scoped Fixtures ...">


@pytest.fixture(scope="session", autouse=True)
def anyio_backend() -> tuple[str, dict[str, bool]]:
    """Set the asyncio backend for the test suite."""
    return "asyncio", {"use_uvloop": True}


@pytest.fixture(scope="session")
def api_client() -> Generator[AsyncClient, None, None]:
    """A session-scoped, pre-configured `httpx.AsyncClient` instance."""
    client = AsyncClient(
        app=app,
        base_url="http://api.example.testing",
    )

    yield client

    del client


# </editor-fold desc="# Auto-used, Session-scoped Fixtures ...">

# <editor-fold desc="# Function-scoped Fixtures ...">

# </editor-fold desc="# Function-scoped Fixtures ...">
