from typing import Optional
from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Description
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import PokemonSpecies, Region, VersionGroup


class Pokedex(NamedResource):
    descriptions: List["Description"]
    is_main_series: bool
    pokemon_entries: List["PokemonEntry"]
    region: Optional[MinimalResource["Region"]]
    version_groups: List[MinimalResource["VersionGroup"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.descriptions = [
            Description(description_data) for description_data in data["descriptions"]
        ]
        self.is_main_series = data["is_main_series"]
        self.pokemon_entries = [
            PokemonEntry(pokemon_entry_data)
            for pokemon_entry_data in data["pokemon_entries"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.region = (
            MinimalResource(data["region"]) if data["region"] is not None else None
        )
        self.version_groups = [
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        ]


class PokemonEntry(Resource):
    entry_number: int
    pokemon_species: MinimalResource["PokemonSpecies"]

    def __init__(self, data) -> None:
        self.entry_number = data["entry_number"]
        self.pokemon_species = MinimalResource(data["pokemon_species"])
