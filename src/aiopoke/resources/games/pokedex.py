from typing import TYPE_CHECKING, Optional, Tuple

from ...minimal_resources import MinimalResource
from ...utility import Description, Name, NamedResource

if TYPE_CHECKING:
    from ...resources import PokemonSpecies, Region, VersionGroup


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

    def __repr__(self) -> str:
        return (
            f"<Pokedex description={self.description} descriptions={self.descriptions} id_={self.id_} "
            f"is_main_series={self.is_main_series} name='{self.name}' pokemon_entries={self.pokemon_entries} "
            f"names={self.names} region={self.region} version_groups={self.version_groups}>"
        )


class PokemonEntry:
    entry_number: int
    pokemon_species: MinimalResource["PokemonSpecies"]

    def __init__(self, data) -> None:
        self.entry_number = data["entry_number"]
        self.pokemon_species = MinimalResource(data["pokemon_species"])

    def __repr__(self) -> str:
        return f"<PokemonEntry entry_number={self.entry_number} pokemon_species={self.pokemon_species}>"
