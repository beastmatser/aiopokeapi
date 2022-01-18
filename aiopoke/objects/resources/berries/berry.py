from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import BerryFirmness, BerryFlavor
    from aiopoke.objects.resources.items.item import Item
    from aiopoke.objects.resources.pokemon.natural_gift_type import NaturalGiftType


class Berry(NamedResource):
    firmness: MinimalResource["BerryFirmness"]
    flavors: List["BerryFlavorMap"]
    item: MinimalResource["Item"]
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    natural_gift_type: MinimalResource["NaturalGiftType"]
    soil_dryness: int
    smoothness: int
    size: int

    def __init__(
        self,
        *,
        id: int,
        name: str,
        firmness: Dict[str, Any],
        flavors: List[Dict[str, Any]],
        item: Dict[str, Any],
        growth_time: int,
        max_harvest: int,
        natural_gift_power: int,
        natural_gift_type: Dict[str, Any],
        soil_dryness: int,
        smoothness: int,
        size: int
    ) -> None:
        super().__init__(id=id, name=name)
        self.firmness = MinimalResource(**firmness)
        self.flavors = [BerryFlavorMap(**flavor) for flavor in flavors]
        self.item = MinimalResource(**item)
        self.growth_time = growth_time
        self.max_harvest = max_harvest
        self.natural_gift_power = natural_gift_power
        self.natural_gift_type = MinimalResource(**natural_gift_type)
        self.soil_dryness = soil_dryness
        self.smoothness = smoothness
        self.size = size


class BerryFlavorMap(Resource):
    potency: int
    flavor: MinimalResource["BerryFlavor"]

    def __init__(self, *, potency: int, flavor: Dict[str, Any]) -> None:
        self.potency = potency
        self.flavor = MinimalResource(**flavor)
