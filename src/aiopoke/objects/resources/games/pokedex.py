from typing import TYPE_CHECKING, Any, Dict, List, Optional

from aiopoke.objects.utility import Description, Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import PokemonSpecies, Region, VersionGroup


class Pokedex(NamedResource):
    descriptions: List["Description"]
    is_main_series: bool
    pokemon_entries: List["PokemonEntry"]
    region: Optional[MinimalResource["Region"]]
    version_groups: List[MinimalResource["VersionGroup"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        descriptions: List[Dict[str, Any]],
        is_main_series: bool,
        pokemon_entries: List[Dict[str, Any]],
        region: Optional[Dict[str, Any]],
        version_groups: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.descriptions = [Description(**description) for description in descriptions]
        self.is_main_series = is_main_series
        self.pokemon_entries = [
            PokemonEntry(**pokemon_entry) for pokemon_entry in pokemon_entries
        ]
        self.region = MinimalResource(**region) if region is not None else None
        self.version_groups = [
            MinimalResource(**version_group) for version_group in version_groups
        ]
        self.names = [Name(**name) for name in names]


class PokemonEntry(Resource):
    entry_number: int
    pokemon_species: MinimalResource["PokemonSpecies"]

    def __init__(self, *, entry_number: int, pokemon_species: Dict[str, Any]) -> None:
        self.entry_number = entry_number
        self.pokemon_species = MinimalResource(**pokemon_species)
