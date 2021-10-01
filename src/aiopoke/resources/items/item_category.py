from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from . import Item, ItemPocket


class ItemCategory(NamedResource):
    items: List[MinimalResource["Item"]]
    names: List["Name"]
    pocket: MinimalResource["ItemPocket"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.items = [MinimalResource(item_data) for item_data in data["items"]]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.pocket = MinimalResource(data["pocket"])

    def __repr__(self) -> str:
        return f"<ItemCategory id_{self.id_} items={self.items} name='{self.name}' names={self.names} pocket={self.pocket}>"
