from typing import List
from ...minimal_resources import MinimalItemCategory
from ...utility.common_models import Name, NamedResource


class ItemPocket(NamedResource):
    categories: List["MinimalItemCategory"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.categories = [MinimalItemCategory(item_category_data) for item_category_data in data["categories"]]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<ItemPocket categories={self.categories} id_={self.id_} name='{self.name}' names={self.names}>"
