"""The example's endpoint handlers."""

# Future Imports
from __future__ import annotations

# Standard Library Imports
from http import HTTPStatus
from typing import Annotated

# Third-Party Imports
from fastapi import (
    Path,
    Query,
)

# Package-Level Imports
from example_models.item import (
    Item,
    ItemUpdateResponse,
)

# Imports From Package Sub-Modules
from .core import app

__all__ = ("root",)

# <editor-fold desc="# Type Definitions ...">

ItemID = Annotated[
    int,
    Path(ge=0, le=1000, title="The ID of the item to update"),
]
CreateFlag = Annotated[
    bool,
    Query(
        description="Indicates a request to update item that does not"
        " exist should create a new item instead of returning an error",
        examples=[1, 0, True, False],
    ),
]

# </editor-fold desc="# Type Definitions ...">

# <editor-fold desc="# Endpoint Functions ...">


@app.get("/")
async def root() -> dict[str, str]:
    """The standard "hello world" root handler."""
    return {"hello": "world"}


@app.post(
    "/items/{item_id}",
    status_code=HTTPStatus.ACCEPTED,
)
async def update_item(
    item_id: ItemID,
    create: CreateFlag = False,
    item: Item | None = None,
) -> ItemUpdateResponse:
    return {
        "item": item,
        "create": create,
        "item_id": item_id,
    }


# </editor-fold desc="# Endpoint Functions ...">
