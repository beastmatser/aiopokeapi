from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.items import ItemCategory


class ItemPocket(NamedResource):
    categories: List[MinimalResource["ItemCategory"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.categories = [
            MinimalResource(item_category_data)
            for item_category_data in data["categories"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
