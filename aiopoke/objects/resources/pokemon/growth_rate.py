from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        descriptions: List[Dict[str, Any]],
        formula: str,
        levels: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.descriptions = [Description(**description) for description in descriptions]
        self.formula = formula
        self.levels = [GrowthRateExperienceLevel(**level) for level in levels]
        self.pokemon_species = [
            MinimalResource(**pokemon_species) for pokemon_species in pokemon_species
        ]


class GrowthRateExperienceLevel(Resource):
    level: int
    experience: int

    def __init__(self, *, level: int, experience: int) -> None:
        self.level = level
        self.experience = experience
