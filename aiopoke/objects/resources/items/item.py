from typing import TYPE_CHECKING, Any, Dict, List, Optional

from aiopoke.objects.utility import (
    GenerationGameIndex,
    MachineVersionDetail,
    Name,
    NamedResource,
    Sprite,
    VerboseEffect,
    VersionGroupFlavorText,
)
from aiopoke.utils.minimal_resources import MinimalResource, Url
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import EvolutionChain, Pokemon, Version
    from aiopoke.objects.resources.items import (
        ItemAttribute,
        ItemCategory,
        ItemFlingEffect,
    )


class Item(NamedResource):
    attributes: List[MinimalResource["ItemAttribute"]]
    baby_trigger_for: Optional[Url["EvolutionChain"]]
    category: MinimalResource["ItemCategory"]
    cost: int
    effect_entries: List["VerboseEffect"]
    flavor_text_entries: List["VersionGroupFlavorText"]
    fling_effect: Optional[MinimalResource["ItemFlingEffect"]]
    fling_power: Optional[int]
    game_indices: List["GenerationGameIndex"]
    held_by_pokemon: List["ItemHolderPokemon"]
    machines: List["MachineVersionDetail"]
    names: List["Name"]
    sprite: Optional["ItemSprites"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        attributes: List[Dict[str, Any]],
        baby_trigger_for: Optional[Dict[str, Any]],
        category: Dict[str, Any],
        cost: int,
        effect_entries: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
        fling_effect: Optional[Dict[str, Any]],
        fling_power: Optional[int],
        game_indices: List[Dict[str, Any]],
        held_by_pokemon: List[Dict[str, Any]],
        machines: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        sprites: Optional[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.attributes = [MinimalResource(**attribute) for attribute in attributes]
        self.baby_trigger_for = (
            Url(**baby_trigger_for) if baby_trigger_for is not None else None
        )
        self.category = MinimalResource(**category)
        self.cost = cost
        self.effect_entries = [
            VerboseEffect(**effect_entry) for effect_entry in effect_entries
        ]
        self.flavor_text_entries = [
            VersionGroupFlavorText(**flavor_text_entry)
            for flavor_text_entry in flavor_text_entries
        ]
        self.fling_effect = Url(**fling_effect) if fling_effect is not None else None  # type: ignore
        self.fling_power = fling_power
        self.game_indices = [
            GenerationGameIndex(**game_index) for game_index in game_indices
        ]
        self.held_by_pokemon = [
            ItemHolderPokemon(**held_by_pokemon) for held_by_pokemon in held_by_pokemon
        ]
        self.machines = [MachineVersionDetail(**machine) for machine in machines]
        self.names = [Name(**name) for name in names]
        self.sprite = ItemSprites(**sprites) if sprites is not None else None


class ItemSprites(Resource):
    default: Optional["Sprite"]

    def __init__(self, *, default: Optional[str]) -> None:
        self.default = Sprite(default) if default is not None else None


class ItemHolderPokemon(Resource):
    pokemon: MinimalResource["Pokemon"]
    version_details: List["ItemHolderPokemonVersionDetail"]

    def __init__(
        self,
        *,
        pokemon: Dict[str, Any],
        version_details: List[Dict[str, Any]],
    ) -> None:
        self.pokemon = MinimalResource(**pokemon)
        self.version_details = [
            ItemHolderPokemonVersionDetail(**version_detail)
            for version_detail in version_details
        ]


class ItemHolderPokemonVersionDetail(Resource):
    rarity: int
    version: MinimalResource["Version"]

    def __init__(self, *, rarity: int, version: Dict[str, Any]) -> None:
        self.rarity = rarity
        self.version = MinimalResource(**version)
