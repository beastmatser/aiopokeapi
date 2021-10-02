from typing import TYPE_CHECKING, Optional, Tuple

from ...minimal_resources import MinimalResource, Url
from ...utility import (
    FlavorText,
    GenerationGameIndex,
    MachineVersionDetail,
    Name,
    NamedResource,
    Sprite,
    VerboseEffect,
)

if TYPE_CHECKING:
    from ...resources import EvolutionChain, Pokemon, Version
    from . import ItemAttribute, ItemCategory, ItemFlingEffect


class Item(NamedResource):
    attributes: Tuple[MinimalResource["ItemAttribute"]]
    baby_trigger_for: Optional[Url["EvolutionChain"]]
    category: MinimalResource["ItemCategory"]
    cost: int
    effect_entry: "VerboseEffect"
    effect_entries: Tuple["VerboseEffect"]
    flavor_text_entry: "FlavorText"
    flavor_text_entries: Tuple["FlavorText"]
    fling_effect: Optional[MinimalResource["ItemFlingEffect"]]
    fling_power: Optional[int]
    game_indices: Tuple["GenerationGameIndex"]
    held_by_pokemon: Tuple["ItemHolderPokemon"]
    machines: Tuple["MachineVersionDetail"]
    names: Tuple["Name"]
    sprite: Optional["Sprite"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.attributes = tuple(
            MinimalResource(attribute_data) for attribute_data in data["attributes"]
        )
        self.baby_trigger_for = (
            Url(data["baby_trigger_for"]["url"])
            if data["baby_trigger_for"] is not None
            else None
        )
        self.category = MinimalResource(data["category"])
        self.cost = data["cost"]
        self.effect_entry = tuple(
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        )[0]
        self.effect_entries = tuple(
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        )
        self.flavor_text_entry = tuple(
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        )[0]
        self.flavor_text_entries = tuple(
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        )
        self.fling_effect = (
            MinimalResource(data["fling_effect"])
            if data["fling_effect"] is not None
            else None
        )
        self.fling_power = data["fling_power"]
        self.game_indices = tuple(
            GenerationGameIndex(game_indice_data)
            for game_indice_data in data["game_indices"]
        )
        self.held_by_pokemon = tuple(
            ItemHolderPokemon(pokemon_data) for pokemon_data in data["held_by_pokemon"]
        )
        self.machines = tuple(
            MachineVersionDetail(machine_data) for machine_data in data["machines"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.sprite = Sprite(data["sprites"]["default"])

    def __repr__(self) -> str:
        return (
            f"<Item attributes={self.attributes} baby_trigger_form={self.baby_trigger_for} cost={self.cost} effect_entry={self.effect_entry} "
            f"effect_entries={self.effect_entries} flavor_text_entry={self.flavor_text_entry} flavor_text_entries={self.flavor_text_entries} "
            f"fling_effect={self.fling_effect} fling_power={self.fling_power} game_indices={self.game_indices} held_by_pokemon={self.held_by_pokemon} "
            f"id_={self.id_} machines={self.machines} name='{self.name}' names={self.name} sprite={self.sprite}>"
        )


class ItemSprites:
    default: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.default = Sprite.from_url(data["default"])

    def __repr__(self) -> str:
        return f"<ItemSprites default={self.default}>"


class ItemHolderPokemon:
    pokemon: MinimalResource["Pokemon"]
    version_details: Tuple["ItemHolderPokemonVersionDetail"]

    def __init__(self, data) -> None:
        self.pokemon = MinimalResource(data["pokemon"])
        self.version_details = tuple(
            ItemHolderPokemonVersionDetail(version_detail_data)
            for version_detail_data in data["version_details"]
        )

    def __repr__(self) -> str:
        return f"<ItemHolderPokemon pokemon={self.pokemon} version_details={self.version_details}>"


class ItemHolderPokemonVersionDetail:
    rarity: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.rarity = data["rarity"]
        self.version = MinimalResource(data["version"])

    def __repr__(self) -> str:
        return f"<ItemHolderPokemonVersionDetail rarity={self.rarity} version={self.version}>"
