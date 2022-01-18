from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility import Description, Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Item


class ItemAttribute(NamedResource):
    descriptions: List["Description"]
    items: List[MinimalResource["Item"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        descriptions: List[Dict[str, Any]],
        items: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        self.descriptions = [Description(**description) for description in descriptions]
        self.items = [MinimalResource(**item) for item in items]
        self.names = [Name(**name) for name in names]
