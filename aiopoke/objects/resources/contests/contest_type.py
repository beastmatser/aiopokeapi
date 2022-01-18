from typing import TYPE_CHECKING, List

from aiopoke.objects.utility import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import BerryFlavor


class ContestType(NamedResource):
    berry_flavor: MinimalResource["BerryFlavor"]
    names: List["ContestName"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berry_flavor = MinimalResource(data["berry_flavor"])
        self.names = [ContestName(name_data) for name_data in data["names"]]


class ContestName(Name):
    color: str

    def __init__(self, data) -> None:
        super().__init__(data)
        self.color = data["color"]
