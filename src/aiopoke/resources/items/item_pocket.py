from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from . import ItemCategory


class ItemPocket(NamedResource):
    categories: List[MinimalResource["ItemCategory"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.categories = [MinimalResource(item_category_data) for item_category_data in data["categories"]]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<ItemPocket categories={self.categories} id_={self.id_} name='{self.name}' names={self.names}>"
