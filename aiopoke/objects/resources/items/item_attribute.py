from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import Description
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Item


class ItemAttribute(NamedResource):
    description: str
    descriptions: Tuple["Description", ...]
    items: Tuple[MinimalResource["Item"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = tuple(
            description_data["description"]
            for description_data in data["descriptions"]
            if description_data["language"]["name"] == "en"
        )[0]
        self.descriptions = tuple(
            Description(description_data) for description_data in data["descriptions"]
        )
        self.items = tuple(MinimalResource(item_data) for item_data in data["items"])
        self.names = tuple(Name(name_data) for name_data in data["names"])
