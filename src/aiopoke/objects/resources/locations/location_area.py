from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import Name, NamedResource, VersionEncounterDetail
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import EncounterMethod, Pokemon, Version
    from aiopoke.objects.resources.locations import Location


class LocationArea(NamedResource):
    encounter_method_rates: List["EncounterMethodRate"]
    pokemon_encounters: List["PokemonEncounter"]
    location: MinimalResource["Location"]
    game_index: int
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        encounter_method_rates: List[Dict[str, Any]],
        pokemon_encounters: List[Dict[str, Any]],
        location: Dict[str, Any],
        game_index: int,
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.encounter_method_rates = [
            EncounterMethodRate(**encounter_method_rate)
            for encounter_method_rate in encounter_method_rates
        ]
        self.pokemon_encounters = [
            PokemonEncounter(**pokemon_encounter)
            for pokemon_encounter in pokemon_encounters
        ]
        self.location = MinimalResource(**location)
        self.game_index = game_index
        self.names = [Name(**name) for name in names]


class PokemonEncounter(Resource):
    pokemon: MinimalResource["Pokemon"]
    version_details: List["VersionEncounterDetail"]

    def __init__(
        self,
        *,
        pokemon: Dict[str, Any],
        version_details: List[Dict[str, Any]],
    ) -> None:
        self.pokemon = MinimalResource(**pokemon)
        self.version_details = [
            VersionEncounterDetail(**version_encounter_detail)
            for version_encounter_detail in version_details
        ]


class EncounterMethodRate(Resource):
    encounter_method: MinimalResource["EncounterMethod"]
    version_details: List["EncounterVersionDetail"]

    def __init__(
        self,
        *,
        encounter_method: Dict[str, Any],
        version_details: List[Dict[str, Any]],
    ) -> None:
        self.encounter_method = MinimalResource(**encounter_method)
        self.version_details = [
            EncounterVersionDetail(**version_encounter_detail)
            for version_encounter_detail in version_details
        ]


class EncounterVersionDetail(Resource):
    rate: int
    version: MinimalResource["Version"]

    def __init__(
        self,
        *,
        rate: int,
        version: Dict[str, Any],
    ) -> None:
        self.rate = rate
        self.version = MinimalResource(**version)
