from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from . import PokemonSpecies


class EggGroup(NamedResource):
    pokemon_species: List[MinimalResource["PokemonSpecies"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.pokemon_species = [
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<EggGroup id_={self.id_} pokemon_species={self.pokemon_species} name='{self.name}' names={self.names}>"
