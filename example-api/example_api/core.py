"""The example's "core" FastAPI instance."""

# Future Imports
from __future__ import annotations

# Third-Party Imports
from fastapi import FastAPI

__all__ = ("app",)

app: FastAPI = FastAPI(
    debug=True,
    version=__import__("example_api").__version__,
    title="""Python "Workspace" Repository Example""",
)
