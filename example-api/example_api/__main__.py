"""A super simple example of using FastAPI in a "workspace"-style repository
pattern."""

# Future Imports
from __future__ import annotations

# Standard Library Imports
from operator import methodcaller
from pathlib import Path

# Third-Party Imports
import more_itertools as mi
import uvicorn
import uvicorn.supervisors


def get_reload_dirs() -> list[str]:
    """Find the on-disk paths of all of the workspace's locally installed
    "components"."""

    components = list()

    for component in map("example%s".__mod__, ("", "_api", "_jobs", "_common", "_models")):
        try:
            components.append(Path(__import__(component).__file__).parent)
        except (ImportError, ModuleNotFoundError):
            pass

    component_dirs = set(
        map(
            lambda path: str(path).removesuffix("/__pycache__"),
            filter(
                Path.is_dir,
                mi.collapse(
                    map(methodcaller("rglob", "**/*"), components),
                    base_type=Path,
                ),
            ),
        )
    )

    return list(component_dirs)


def serve_api() -> None:
    """Serve the workspace's FastAPI app with uvicorn."""

    reload_dirs = get_reload_dirs()

    server = uvicorn.Server(
        uvicorn.Config(
            "example_api.core:app",
            host="::",
            port=8080,
            loop="uvloop",
            log_level="debug",
            reload=bool(reload_dirs),
            reload_dirs=reload_dirs or None,
        ),
    )

    server.run()


if __name__ == "__main__":
    serve_api()
