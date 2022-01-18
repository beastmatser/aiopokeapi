from typing import Tuple

from aiopoke.objects.utility.common_models import Description
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource


class EncounterMethod(NamedResource):
    description: str
    descriptions: Tuple["Description", ...]
    order: int
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = tuple(
            name_data["name"]
            for name_data in data["names"]
            if name_data["language"]["name"] == "en"
        )[0]
        self.descriptions = tuple(
            Description(description_data) for description_data in data["descriptions"]
        )
        self.order = data["order"]
        self.names = tuple(Name(name_data) for name_data in data["names"])
