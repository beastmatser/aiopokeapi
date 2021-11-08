from typing import Tuple
from typing import TYPE_CHECKING

from ...minimal_resources import MinimalResource
from ...utility import Description
from ...utility import Name
from ...utility import NamedResource

if TYPE_CHECKING:
    from ...resources import Item


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

    def __repr__(self) -> str:
        return (
            f"<ItemAttribute description='{self.description}' descriptions={self.descriptions} id_={self.id_} "
            f"items={self.items} names={self.names}>"
        )
