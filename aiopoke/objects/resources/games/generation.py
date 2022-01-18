from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

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
    abilities: Tuple[MinimalResource["Ability"], ...]
    main_region: MinimalResource["Region"]
    moves: Tuple[MinimalResource["Move"], ...]
    pokemon_species: Tuple[MinimalResource["PokemonSpecies"], ...]
    types: Tuple[MinimalResource["NaturalGiftType"], ...]
    version_groups: Tuple[MinimalResource["VersionGroup"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.abilities = tuple(
            MinimalResource(ability_data) for ability_data in data["abilities"]
        )
        self.main_region = MinimalResource(data["main_region"])
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.moves = tuple(MinimalResource(move_data) for move_data in data["moves"])
        self.pokemon_species = tuple(
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        )
        self.types = tuple(MinimalResource(type_data) for type_data in data["types"])
        self.version_groups = tuple(
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        )
