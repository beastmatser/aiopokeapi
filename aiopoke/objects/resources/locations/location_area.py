from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.objects.utility import VersionEncounterDetail
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import EncounterMethod, Pokemon, Version
    from aiopoke.objects.resources.locations import Location


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


class PokemonEncounter(Resource):
    pokemon: MinimalResource["Pokemon"]
    version_details: List["VersionEncounterDetail"]

    def __init__(self, data) -> None:
        self.pokemon = MinimalResource(data["pokemon"])
        self.version_details = [
            VersionEncounterDetail(version_detail_data)
            for version_detail_data in data["version_details"]
        ]


class EncounterMethodRate(Resource):
    encounter_method: MinimalResource["EncounterMethod"]
    version_details: List["EncounterVersionDetail"]

    def __init__(self, data) -> None:
        self.encounter_method = MinimalResource(data["encounter_method"])
        self.version_details = [
            EncounterVersionDetail(encounter_version_detail)
            for encounter_version_detail in data["version_details"]
        ]


class EncounterVersionDetail(Resource):
    rate: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.rate = data["rate"]
        self.version = MinimalResource(data["version"])
