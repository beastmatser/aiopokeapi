from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from . import PokemonSpecies


class PokemonColor(NamedResource):
    names: List["Name"]
    pokemon_species: List[MinimalResource["PokemonSpecies"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.names = [Name(name_data) for name_data in data["names"]]
        self.pokemon_species = [
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        ]

    def __repr__(self) -> str:
        return f"<PokemonColor id_={self.id_} name='{self.name}' names={self.names} pokemon_species={self.pokemon_species}>"
