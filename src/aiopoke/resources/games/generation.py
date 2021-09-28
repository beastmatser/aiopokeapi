from typing import List
from ...minimal_resources import (
    MinimalAbility,
    MinimalNaturalGiftType,
    MinimalRegion,
    MinimalMove,
    MinimalPokemonSpecies,
    MinimalVersionGroup,
)
from ...utility.common_models import Name, NamedResource


class Generation(NamedResource):
    abilities: List["MinimalAbility"]
    main_region: "MinimalRegion"
    moves: List["MinimalMove"]
    pokemon_species: List["MinimalPokemonSpecies"]
    types: List["MinimalNaturalGiftType"]
    version_groups: List["MinimalVersionGroup"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.abilities = [
            MinimalAbility(ability_data) for ability_data in data["abilities"]
        ]
        self.main_region = MinimalRegion(data["main_region"])
        self.names = [Name(name_data) for name_data in data["names"]]
        self.moves = [MinimalMove(move_data) for move_data in data["moves"]]
        self.pokemon_species = [
            MinimalPokemonSpecies(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        ]
        self.types = [MinimalNaturalGiftType(type_data) for type_data in data["types"]]
        self.version_groups = [
            MinimalVersionGroup(version_group_data)
            for version_group_data in data["version_groups"]
        ]

    def __repr__(self) -> str:
        return (
            f"<Generation abilities={self.abilities} id_={self.id_} main_region={self.main_region} "
            f"moves={self.moves} name='{self.name}' pokemon_species={self.pokemon_species} "
            f"types={self.types} version_groups={self.version_groups}"
        )
