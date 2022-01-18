from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import NamedResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon.natural_gift_type import NaturalGiftType
    from aiopoke.objects.resources.berries import BerryFlavor, BerryFirmness


class Berry(NamedResource):
    firmness: MinimalResource["BerryFirmness"]
    flavors: Tuple["BerryFlavorMap", ...]
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    natural_gift_type: MinimalResource["NaturalGiftType"]
    soil_dryness: int
    smoothness: int
    size: int

    def __init__(self, data) -> None:
        super().__init__(data)
        self.firmness = MinimalResource(data["firmness"])
        self.flavors = tuple(
            BerryFlavorMap(flavor_data) for flavor_data in data["flavors"]
        )
        self.growth_time = data["growth_time"]
        self.max_harvest = data["max_harvest"]
        self.natural_gift_power = data["natural_gift_power"]
        self.natural_gift_type = MinimalResource(data["natural_gift_type"])
        self.soil_dryness = data["soil_dryness"]
        self.smoothness = data["smoothness"]
        self.size = data["size"]


class BerryFlavorMap(Resource):
    potency: int
    flavor: MinimalResource["BerryFlavor"]

    def __init__(self, data) -> None:
        self.potency = data["potency"]
        self.flavor = MinimalResource(data["flavor"])
