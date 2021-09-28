from typing import List
from ...minimal_resources import (
    MinimalPokemon,
    MinimalNaturalGiftType,
    MinimalVersionGroup,
)
from ...utility import Name, NamedResource
from ...utility.common_models.sprites import Sprites


class PokemonForm(NamedResource):
    form_name: str
    form_order: int
    is_battle_only: bool
    is_default: bool
    is_mega: bool
    order: int
    names: List["Name"]
    pokemon: "MinimalPokemon"
    sprites: "Sprites"
    types: List["SlotNaturalGiftType"]
    version_group: "MinimalVersionGroup"

    def __init__(self, data) -> None:
        super().__init__(data)
        self.form_name = data["form_name"]
        self.form_order = data["form_order"]
        self.is_battle_only = data["is_battle_only"]
        self.is_default = data["is_default"]
        self.is_mega = data["is_mega"]
        self.order = data["order"]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.pokemon = MinimalPokemon(data["pokemon"])
        self.sprites = Sprites(data["sprites"])
        self.types = [SlotNaturalGiftType(type_data) for type_data in data["types"]]
        self.version_group = MinimalVersionGroup(data["version_group"])

    def __repr__(self) -> str:
        return (
            f"<PokemonForm form_name='{self.form_name}' form_order={self.form_order} id_={self.id_} is_battle_only={self.is_battle_only} "
            f"is_default={self.is_default} is_mega={self.is_mega} order={self.order} name='{self.name}' names={self.names} "
            f"pokemon={self.pokemon} sprites={self.sprites} types={self.types} version_group={self.version_group}>"
        )


class SlotNaturalGiftType:
    type_: MinimalNaturalGiftType
    slot: int

    def __init__(self, data) -> None:
        self.type_ = MinimalNaturalGiftType(data["type"])
        self.slot = data["slot"]

    def __repr__(self) -> str:
        return f"<SlotNaturalGiftType type_={self.type_} slot={self.slot}>"
