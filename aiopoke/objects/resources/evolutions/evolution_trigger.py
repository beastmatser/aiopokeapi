from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import PokemonSpecies


class EvolutionTrigger(NamedResource):
    pokemon_species: Tuple[MinimalResource["PokemonSpecies"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.pokemon_species = tuple(
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
