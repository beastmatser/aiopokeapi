from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource
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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        abilities: List[Dict[str, Any]],
        main_region: Dict[str, Any],
        moves: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]],
        types: List[Dict[str, Any]],
        version_groups: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.abilities = [MinimalResource(**ability) for ability in abilities]
        self.main_region = MinimalResource(**main_region)
        self.moves = [MinimalResource(**move) for move in moves]
        self.pokemon_species = [
            MinimalResource(**pokemon_species) for pokemon_species in pokemon_species
        ]
        self.types = [MinimalResource(**type_) for type_ in types]
        self.version_groups = [
            MinimalResource(**version_group) for version_group in version_groups
        ]
        self.names = [Name(**name) for name in names]
