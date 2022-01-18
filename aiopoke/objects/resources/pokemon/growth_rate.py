from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Description
from aiopoke.objects.utility import NamedResource
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


class GrowthRate(NamedResource):
    descriptions: List["Description"]
    formula: str
    levels: List["GrowthRateExperienceLevel"]
    pokemon_species: List[MinimalResource["PokemonSpecies"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.descriptions = [
            Description(description_data) for description_data in data["descriptions"]
        ]
        self.formula = data["formula"]
        self.levels = [
            GrowthRateExperienceLevel(level_data) for level_data in data["levels"]
        ]
        self.pokemon_species = [
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        ]


class GrowthRateExperienceLevel(Resource):
    level: int
    experience: int

    def __init__(self, data) -> None:
        self.level = data["level"]
        self.experience = data["experience"]
