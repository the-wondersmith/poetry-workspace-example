"""A super simple "item" model for the workspace's api "component"."""

# Future Imports
from __future__ import annotations

# Third-Party Imports
from pydantic import (
    BaseModel,
    Field,
)
from typing_extensions import TypedDict

__all__ = (
    "Item",
    "ItemUpdateResponse",
)


class Item(BaseModel):
    """A contrived "item" for the workspace's api "component"."""

    # <editor-fold desc="# Model Fields ...">

    name: str = Field(
        ...,
        min_length=3,
        description="The item's human-readable name",
        examples=[
            "soap",
            "pickle",
            "oblong orb",
        ],
    )
    tax: float | None = Field(
        default=None,
        description="The compulsory contribution to state "
        "revenue levied by the government against the item's base cost",
        examples=[64.74, 272.81, 5473.25],
    )
    price: float = Field(
        ...,
        description="The item's monetary (purchase) cost",
        examples=[94.93, 512.98, 7465.55],
    )
    description: str | None = Field(
        default=None,
        description="The item's human-readable 'sales pitch'-style definition",
        examples=[
            "Plush leather armchair, barely used, adds luxury to any room.",
            "Handmade oak-wood dining table, crafted for modern minimalistic homes.",
            "Vintage bicycle in excellent condition, perfect for enthusiastic riders.",
        ],
    )

    # </editor-fold desc="# Model Fields ...">

    # <editor-fold desc="# Properties ...">

    @property
    def total(self) -> float:
        """The item's purchase total."""
        return round(self.price + self.tax, 2)

    # </editor-fold desc="# Properties ...">


class ItemUpdateResponse(TypedDict, total=False):
    """A response to a request to update a specific `Item`."""

    create: bool
    item_id: int
    item: Item | None
