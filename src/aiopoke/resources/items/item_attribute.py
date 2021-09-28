from typing import List
from ...minimal_resources import MinimalItem
from ...utility import Name, NamedResource, Description


class ItemAttribute(NamedResource):
    description: str
    descriptions: List["Description"]
    items: List["MinimalItem"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = [description_data["description"] for description_data in data["descriptions"] if description_data["language"]["name"] == "en"][0]
        self.descriptions = [Description(description_data) for description_data in data["descriptions"]]
        self.items = [MinimalItem(item_data) for item_data in data["items"]]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return (
            f"<ItemAttribute description='{self.description}' descriptions={self.descriptions} id_={self.id_} "
            f"items={self.items} names={self.names}>"
        )
