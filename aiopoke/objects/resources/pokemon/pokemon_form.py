from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import Name, NamedResource, Sprites
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import NaturalGiftType, VersionGroup
    from aiopoke.objects.resources.pokemon import Pokemon


class PokemonForm(NamedResource):
    form_name: str
    form_names: List["Name"]
    form_order: int
    is_battle_only: bool
    is_default: bool
    is_mega: bool
    order: int
    names: List["Name"]
    pokemon: MinimalResource["Pokemon"]
    sprites: "Sprites"
    types: List["SlotNaturalGiftType"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        form_name: str,
        form_names: List[Dict[str, Any]],
        form_order: int,
        is_battle_only: bool,
        is_default: bool,
        is_mega: bool,
        order: int,
        names: List[Dict[str, Any]],
        pokemon: Dict[str, Any],
        sprites: Dict[str, Any],
        types: List[Dict[str, Any]],
        version_group: Dict[str, Any],
    ) -> None:
        super().__init__(id=id, name=name)
        self.form_name = form_name
        self.form_names = [Name(**name) for name in form_names]
        self.form_order = form_order
        self.is_battle_only = is_battle_only
        self.is_default = is_default
        self.is_mega = is_mega
        self.order = order
        self.names = [Name(**name) for name in names]
        self.pokemon = MinimalResource(**pokemon)
        self.sprites = Sprites(sprites)
        self.types = [SlotNaturalGiftType(**type_) for type_ in types]
        self.version_group = MinimalResource(**version_group)


class SlotNaturalGiftType(Resource):
    type: MinimalResource[MinimalResource["NaturalGiftType"]]
    slot: int

    def __init__(
        self,
        *,
        type: Dict[str, Any],
        slot: int,
    ) -> None:
        self.type = MinimalResource(**type)
        self.slot = slot
