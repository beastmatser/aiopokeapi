from typing import List

from aiopoke.objects.utility.common_models import Description
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource


class EncounterMethod(NamedResource):
    descriptions: List["Description"]
    order: int
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.descriptions = [
            Description(description_data) for description_data in data["descriptions"]
        ]
        self.order = data["order"]
        self.names = [Name(name_data) for name_data in data["names"]]
