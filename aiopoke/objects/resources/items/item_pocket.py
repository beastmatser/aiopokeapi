from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.items import ItemCategory


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
