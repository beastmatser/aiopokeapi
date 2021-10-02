from typing import TYPE_CHECKING, Tuple

from ...minimal_resources import MinimalResource
from ...utility import NamedResource

if TYPE_CHECKING:
    from ...resources.pokemon.natural_gift_type import NaturalGiftType
    from . import BerryFlavor, BerryFirmness


class Berry(NamedResource):
    firmness: MinimalResource["BerryFirmness"]
    flavors: Tuple["BerryFlavorMap"]
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
            BerryFlavorMap(flavor_data)
            for flavor_data in data["flavors"]
        )
        self.growth_time = data["growth_time"]
        self.max_harvest = data["max_harvest"]
        self.natural_gift_power = data["natural_gift_power"]
        self.natural_gift_type = MinimalResource(data["natural_gift_type"])
        self.soil_dryness = data["soil_dryness"]
        self.smoothness = data["smoothness"]
        self.size = data["size"]

    def __repr__(self) -> str:
        return (
            f"<Berry firmness='{self.firmness}' flavors={self.flavors} growth_time={self.growth_time} "
            f"id_={self.id_} max_harvest={self.max_harvest} name={self.name} "
            f"natural_gift_power={self.natural_gift_power} natural_gift_type={self.natural_gift_type} "
            f"soil_dryness={self.soil_dryness} smoothness={self.smoothness} size={self.size}>"
        )


class BerryFlavorMap:
    potency: int
    flavor: MinimalResource["BerryFlavor"]

    def __init__(self, data) -> None:
        self.potency = data["potency"]
        self.flavor = MinimalResource(data["flavor"])
