from typing import TYPE_CHECKING, List

from aiopoke.objects.utility import Description, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

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
