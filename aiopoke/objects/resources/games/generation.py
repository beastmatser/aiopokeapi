from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import (
        Ability,
        Move,
        NaturalGiftType,
        PokemonSpecies,
        Region,
        VersionGroup,
    )


class Generation(NamedResource):
    abilities: List[MinimalResource["Ability"]]
    main_region: MinimalResource["Region"]
    moves: List[MinimalResource["Move"]]
    pokemon_species: List[MinimalResource["PokemonSpecies"]]
    types: List[MinimalResource["NaturalGiftType"]]
    version_groups: List[MinimalResource["VersionGroup"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.abilities = [
            MinimalResource(ability_data) for ability_data in data["abilities"]
        ]
        self.main_region = MinimalResource(data["main_region"])
        self.names = [Name(name_data) for name_data in data["names"]]
        self.moves = [MinimalResource(move_data) for move_data in data["moves"]]
        self.pokemon_species = [
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        ]
        self.types = [MinimalResource(type_data) for type_data in data["types"]]
        self.version_groups = [
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        ]
