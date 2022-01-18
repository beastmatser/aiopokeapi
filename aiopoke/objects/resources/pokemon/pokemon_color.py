from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


class PokemonColor(NamedResource):
    names: Tuple["Name", ...]
    pokemon_species: Tuple[MinimalResource["PokemonSpecies"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.pokemon_species = tuple(
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        )

    def __repr__(self) -> str:
        return f"<PokemonColor id_={self.id} name='{self.name}' names={self.names} pokemon_species={self.pokemon_species}>"
