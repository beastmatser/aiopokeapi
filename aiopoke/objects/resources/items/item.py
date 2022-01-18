from typing import TYPE_CHECKING, List, Optional

from aiopoke.objects.utility import (
    FlavorText,
    GenerationGameIndex,
    MachineVersionDetail,
    Name,
    NamedResource,
    Sprite,
    VerboseEffect,
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
    flavor_text_entries: List["FlavorText"]
    fling_effect: Optional[MinimalResource["ItemFlingEffect"]]
    fling_power: Optional[int]
    game_indices: List["GenerationGameIndex"]
    held_by_pokemon: List["ItemHolderPokemon"]
    machines: List["MachineVersionDetail"]
    names: List["Name"]
    sprite: Optional["Sprite"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.attributes = [
            MinimalResource(attribute_data) for attribute_data in data["attributes"]
        ]
        self.baby_trigger_for = (
            Url(data["baby_trigger_for"]["url"])
            if data["baby_trigger_for"] is not None
            else None
        )
        self.category = MinimalResource(data["category"])
        self.cost = data["cost"]
        self.effect_entries = [
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        ]
        self.flavor_text_entries = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.fling_effect = (
            MinimalResource(data["fling_effect"])
            if data["fling_effect"] is not None
            else None
        )
        self.fling_power = data["fling_power"]
        self.game_indices = [
            GenerationGameIndex(game_indice_data)
            for game_indice_data in data["game_indices"]
        ]
        self.held_by_pokemon = [
            ItemHolderPokemon(pokemon_data) for pokemon_data in data["held_by_pokemon"]
        ]
        self.machines = [
            MachineVersionDetail(machine_data) for machine_data in data["machines"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.sprite = Sprite(data["sprites"]["default"])


class ItemSprites(Resource):
    default: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.default = Sprite.from_url(data["default"])


class ItemHolderPokemon(Resource):
    pokemon: MinimalResource["Pokemon"]
    version_details: List["ItemHolderPokemonVersionDetail"]

    def __init__(self, data) -> None:
        self.pokemon = MinimalResource(data["pokemon"])
        self.version_details = [
            ItemHolderPokemonVersionDetail(version_detail_data)
            for version_detail_data in data["version_details"]
        ]


class ItemHolderPokemonVersionDetail(Resource):
    rarity: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.rarity = data["rarity"]
        self.version = MinimalResource(data["version"])
