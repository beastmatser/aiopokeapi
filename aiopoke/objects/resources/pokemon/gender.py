from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import NamedResource
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


class Gender(NamedResource):
    pokemon_species_details: Tuple["PokemonSpeciesGender", ...]
    required_for_evolution: Tuple[MinimalResource["PokemonSpecies"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.pokemon_species_details = tuple(
            PokemonSpeciesGender(pokemon_species_detail_data)
            for pokemon_species_detail_data in data["pokemon_species_details"]
        )
        self.required_for_evolution = tuple(
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["required_for_evolution"]
        )


class PokemonSpeciesGender(Resource):
    pokemon_species: MinimalResource["PokemonSpecies"]
    rate: int

    def __init__(self, data) -> None:
        self.pokemon_species = MinimalResource(data["pokemon_species"])
        self.rate = data["rate"]
