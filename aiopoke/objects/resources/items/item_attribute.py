from typing import TYPE_CHECKING, List

from aiopoke.objects.utility import Description, Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Item


class ItemAttribute(NamedResource):
    descriptions: List["Description"]
    items: List[MinimalResource["Item"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.descriptions = [
            Description(description_data) for description_data in data["descriptions"]
        ]
        self.items = [MinimalResource(item_data) for item_data in data["items"]]
        self.names = [Name(name_data) for name_data in data["names"]]
