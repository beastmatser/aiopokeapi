from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.items import Item, ItemPocket


class ItemCategory(NamedResource):
    items: List[MinimalResource["Item"]]
    names: List["Name"]
    pocket: MinimalResource["ItemPocket"]

    def __init__(
        self,
        *,
        items: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        pocket: Dict[str, Any],
    ) -> None:
        self.items = [MinimalResource(**item) for item in items]
        self.names = [Name(**name) for name in names]
        self.pocket = MinimalResource(**pocket)
