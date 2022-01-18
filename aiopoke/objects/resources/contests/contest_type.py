from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import BerryFlavor


class ContestType(NamedResource):
    berry_flavor: MinimalResource["BerryFlavor"]
    names: Tuple["ContestName", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berry_flavor = MinimalResource(data["berry_flavor"])
        self.names = tuple(ContestName(name_data) for name_data in data["names"])


class ContestName(Name):
    color: str

    def __init__(self, data) -> None:
        super().__init__(data)
        self.color = data["color"]
