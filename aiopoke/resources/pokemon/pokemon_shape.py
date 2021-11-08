from typing import Tuple
from typing import TYPE_CHECKING

from ...minimal_resources import MinimalResource
from ...utility.common_models import Name
from ...utility.common_models import NamedResource

if TYPE_CHECKING:
    from . import PokemonSpecies


class PokemonShape(NamedResource):
    awesome_name: str
    names: Tuple["Name", ...]
    pokemon_species: Tuple[MinimalResource["PokemonSpecies"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.awesome_name = [
            awesome_name_data["awesome_name"]
            for awesome_name_data in data["awesome_names"]
            if awesome_name_data["language"]["name"] == "en"
        ][0]
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.pokemon_species = tuple(
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        )

    def __repr__(self) -> str:
        return f"<PokemonColor awesome_name='{self.awesome_name}' id_={self.id_} name='{self.name}' names={self.names} pokemon_species={self.pokemon_species}>"
