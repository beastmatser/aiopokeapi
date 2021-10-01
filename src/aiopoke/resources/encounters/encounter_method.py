from typing import List
from ...utility.common_models import Name, NamedResource, Description


class EncounterMethod(NamedResource):
    description: str
    descriptions: List["Description"]
    order: int
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = [
            name_data["name"]
            for name_data in data["names"]
            if name_data["language"]["name"] == "en"
        ][0]
        self.descriptions = [Description(description_data) for description_data in data["descriptions"]]
        self.order = data["order"]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return (
            f"<EncounterMethod description='{self.description}' descriptions={self.descriptions} order={self.order} "
            f"id_={self.id_} name='{self.name}' names={self.names}>"
        )
