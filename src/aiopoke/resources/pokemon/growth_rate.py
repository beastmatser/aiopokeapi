from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility import NamedResource, Description

if TYPE_CHECKING:
    from . import PokemonSpecies


class GrowthRate(NamedResource):
    description: str
    descriptions: List["Description"]
    formula: str
    levels: List["GrowthRateExperienceLevel"]
    pokemon_species: List[MinimalResource["PokemonSpecies"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = [
            description_data["description"]
            for description_data in data["descriptions"]
            if description_data["language"]["name"] == "en"
        ][0]
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

    def __repr__(self) -> str:
        return (
            f"<AbilityFlavorText description='{self.description}' descriptions={self.descriptions} formula='{self.formula}' "
            f"id_={self.id_} levels={self.levels} name='{self.name}' pokemon_species={self.pokemon_species}"
        )


class GrowthRateExperienceLevel:
    level: int
    experience: int

    def __init__(self, data) -> None:
        self.level = data["level"]
        self.experience = data["experience"]

    def __repr__(self) -> str:
        return f"<GrowthRateExperienceLevel level={self.level} experience={self.experience}>"
