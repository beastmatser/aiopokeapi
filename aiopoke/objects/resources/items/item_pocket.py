from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.items import ItemCategory


class ItemPocket(NamedResource):
    categories: List[MinimalResource["ItemCategory"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        categories: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        self.categories = [MinimalResource(**category) for category in categories]
        self.names = [Name(**name) for name in names]
