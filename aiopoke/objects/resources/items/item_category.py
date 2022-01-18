from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.items import Item, ItemPocket


class ItemCategory(NamedResource):
    items: Tuple[MinimalResource["Item"], ...]
    names: Tuple["Name", ...]
    pocket: MinimalResource["ItemPocket"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.items = tuple(MinimalResource(item_data) for item_data in data["items"])
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.pocket = MinimalResource(data["pocket"])
