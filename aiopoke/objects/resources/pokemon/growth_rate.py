from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import Description
from aiopoke.objects.utility import NamedResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


class GrowthRate(NamedResource):
    description: str
    descriptions: Tuple["Description", ...]
    formula: str
    levels: Tuple["GrowthRateExperienceLevel", ...]
    pokemon_species: Tuple[MinimalResource["PokemonSpecies"], ...]

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
        self.formula = data["formula"]
        self.levels = tuple(
            GrowthRateExperienceLevel(level_data) for level_data in data["levels"]
        )
        self.pokemon_species = tuple(
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        )


class GrowthRateExperienceLevel(Resource):
    level: int
    experience: int

    def __init__(self, data) -> None:
        self.level = data["level"]
        self.experience = data["experience"]
