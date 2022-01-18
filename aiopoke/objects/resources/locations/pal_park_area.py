from typing import TYPE_CHECKING, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import PokemonSpecies


class PalParkArea(NamedResource):
    pokemon_encounters: List["PalParkEncounterSpecies"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.pokemon_encounters = [
            PalParkEncounterSpecies(pokemon_encounter_data)
            for pokemon_encounter_data in data["pokemon_encounters"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]


class PalParkEncounterSpecies(Resource):
    base_score: int
    rate: int
    pokemon_species: MinimalResource["PokemonSpecies"]

    def __init__(self, data) -> None:
        self.base_score = data["base_score"]
        self.rate = data["rate"]
        self.pokemon_species = MinimalResource(data["pokemon_species"])
