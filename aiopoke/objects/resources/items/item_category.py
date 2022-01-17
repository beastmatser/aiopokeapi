from typing import Tuple
from typing import TYPE_CHECKING

from ....minimal_resources import MinimalResource
from ...utility.common_models import Name
from ...utility.common_models import NamedResource

if TYPE_CHECKING:
    from . import Item, ItemPocket


class ItemCategory(NamedResource):
    items: Tuple[MinimalResource["Item"], ...]
    names: Tuple["Name", ...]
    pocket: MinimalResource["ItemPocket"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.items = tuple(MinimalResource(item_data) for item_data in data["items"])
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.pocket = MinimalResource(data["pocket"])

    def __repr__(self) -> str:
        return f"<ItemCategory id_{self.id} items={self.items} name='{self.name}' names={self.names} pocket={self.pocket}>"
