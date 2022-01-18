from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.objects.utility import Sprites
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import NaturalGiftType, VersionGroup
    from aiopoke.objects.resources.pokemon import Pokemon


class PokemonForm(NamedResource):
    form_name: str
    form_order: int
    is_battle_only: bool
    is_default: bool
    is_mega: bool
    order: int
    names: Tuple["Name", ...]
    pokemon: MinimalResource["Pokemon"]
    sprites: "Sprites"
    types: Tuple["SlotNaturalGiftType", ...]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.form_name = data["form_name"]
        self.form_order = data["form_order"]
        self.is_battle_only = data["is_battle_only"]
        self.is_default = data["is_default"]
        self.is_mega = data["is_mega"]
        self.order = data["order"]
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.pokemon = MinimalResource(data["pokemon"])
        self.sprites = Sprites(data["sprites"])
        self.types = tuple(
            SlotNaturalGiftType(type_data) for type_data in data["types"]
        )
        self.version_group = MinimalResource(data["version_group"])


class SlotNaturalGiftType(Resource):
    type_: MinimalResource[MinimalResource["NaturalGiftType"]]
    slot: int

    def __init__(self, data) -> None:
        self.type_ = MinimalResource(data["type"])
        self.slot = data["slot"]
