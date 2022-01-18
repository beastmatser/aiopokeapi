from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


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
