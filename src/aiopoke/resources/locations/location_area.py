from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource, MinimalPokemon
from ...utility import Name, VersionEncounterDetail, NamedResource

if TYPE_CHECKING:
    from . import Location
    from ...resources import EncounterMethod, Version


class LocationArea(NamedResource):
    encounter_method_rates: List["EncounterMethodRate"]
    pokemon_encounters: List["PokemonEncounter"]
    location: MinimalResource["Location"]
    game_index: int
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.encounter_method_rates = [
            EncounterMethodRate(encounter_method_rate_data)
            for encounter_method_rate_data in data["encounter_method_rates"]
        ]
        self.pokemon_encounters = [
            PokemonEncounter(pokemon_encounter_data)
            for pokemon_encounter_data in data["pokemon_encounters"]
        ]
        self.location = MinimalResource(data["location"])
        self.game_index = data["game_index"]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return (
            f"<LocationArea encounter_method_rates={self.encounter_method_rates} id_={self.id_} pokemon_encounters={self.pokemon_encounters} "
            f"location={self.location} game_index={self.game_index} name='{self.name}' names={self.names}>"
        )


class PokemonEncounter:
    pokemon: "MinimalPokemon"
    version_details: List["VersionEncounterDetail"]

    def __init__(self, data) -> None:
        self.pokemon = MinimalPokemon(data["pokemon"])
        self.version_details = [
            VersionEncounterDetail(version_detail_data)
            for version_detail_data in data["version_details"]
        ]

    def __repr__(self) -> str:
        return f"<PokemonEncounter pokemon={self.pokemon} version_details={self.version_details}>"


class EncounterMethodRate:
    encounter_method: MinimalResource["EncounterMethod"]
    version_details: List["EncounterVersionDetail"]

    def __init__(self, data) -> None:
        self.encounter_method = MinimalResource(data["encounter_method"])
        self.version_details = [
            EncounterVersionDetail(encounter_version_detail)
            for encounter_version_detail in data["version_details"]
        ]

    def __repr__(self) -> str:
        return f"<EncounterMethodRate encounter_method={self.encounter_method} version_details={self.version_details}>"


class EncounterVersionDetail:
    rate: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.rate = data["rate"]
        self.version = MinimalResource(data["version"])

    def __repr__(self) -> str:
        return f"<EncounterVersionDetail rate={self.rate} version={self.version}>"
