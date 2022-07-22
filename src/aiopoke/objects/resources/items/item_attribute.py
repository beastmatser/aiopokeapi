from typing import TYPE_CHECKING, Any, Dict, List

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
        id: int,
        name: str,
        descriptions: List[Dict[str, Any]],
        items: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.descriptions = [Description(**description) for description in descriptions]
        self.items = [MinimalResource(**item) for item in items]
        self.names = [Name(**name) for name in names]
