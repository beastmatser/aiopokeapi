from typing import Tuple
from typing import TYPE_CHECKING

from ...minimal_resources import MinimalResource
from ...utility.common_models import Name
from ...utility.common_models import NamedResource

if TYPE_CHECKING:
    from . import ItemCategory


class ItemPocket(NamedResource):
    categories: Tuple[MinimalResource["ItemCategory"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.categories = tuple(
            MinimalResource(item_category_data)
            for item_category_data in data["categories"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])

    def __repr__(self) -> str:
        return f"<ItemPocket categories={self.categories} id_={self.id} name='{self.name}' names={self.names}>"
