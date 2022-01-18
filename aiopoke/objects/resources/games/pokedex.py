from typing import Optional
from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import Description
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import PokemonSpecies, Region, VersionGroup


class Pokedex(NamedResource):
    description: str
    descriptions: Tuple["Description", ...]
    is_main_series: bool
    pokemon_entries: Tuple["PokemonEntry", ...]
    region: Optional[MinimalResource["Region"]]
    version_groups: Tuple[MinimalResource["VersionGroup"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = tuple(
            description_data["description"]
            for description_data in data["descriptions"]
            if description_data["language"]["name"] == "en"
        )[0]
        self.descriptions = tuple(
            Description(description_data) for description_data in data["descriptions"]
        )
        self.is_main_series = data["is_main_series"]
        self.pokemon_entries = tuple(
            PokemonEntry(pokemon_entry_data)
            for pokemon_entry_data in data["pokemon_entries"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.region = (
            MinimalResource(data["region"]) if data["region"] is not None else None
        )
        self.version_groups = tuple(
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        )


class PokemonEntry(Resource):
    entry_number: int
    pokemon_species: MinimalResource["PokemonSpecies"]

    def __init__(self, data) -> None:
        self.entry_number = data["entry_number"]
        self.pokemon_species = MinimalResource(data["pokemon_species"])
