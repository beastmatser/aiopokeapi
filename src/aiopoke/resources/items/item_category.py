from typing import List
from ...minimal_resources import MinimalItem, MinimalItemPocket
from ...utility.common_models import Name, NamedResource


class ItemCategory(NamedResource):
    items: List["MinimalItem"]
    names: List["Name"]
    pocket: "MinimalItemPocket"

    def __init__(self, data) -> None:
        super().__init__(data)
        self.items = [MinimalItem(item_data) for item_data in data["items"]]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.pocket = MinimalItemPocket(data["pocket"])

    def __repr__(self) -> str:
        return f"<ItemCategory id_{self.id_} items={self.items} name='{self.name}' names={self.names} pocket={self.pocket}>"
