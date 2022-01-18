from typing import TYPE_CHECKING, List

from aiopoke.objects.utility import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import Berry


class BerryFlavor(NamedResource):
    berries: List["FlavorBerryMap"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berries = [FlavorBerryMap(berry_data) for berry_data in data["berries"]]
        self.names = [Name(name_data) for name_data in data["names"]]


class FlavorBerryMap(Resource):
    potency: int
    berry: MinimalResource["Berry"]

    def __init__(self, data) -> None:
        self.potency = data["potency"]
        self.berry = MinimalResource(data["berry"])
