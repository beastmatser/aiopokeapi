from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


class Gender(NamedResource):
    pokemon_species_details: List["PokemonSpeciesGender"]
    required_for_evolution: List[MinimalResource["PokemonSpecies"]]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        pokemon_species_details: List[Dict[str, Any]],
        required_for_evolution: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.pokemon_species_details = [
            PokemonSpeciesGender(**pokemon_species_details)
            for pokemon_species_details in pokemon_species_details
        ]
        self.required_for_evolution = [
            MinimalResource(**required_for_evolution)
            for required_for_evolution in required_for_evolution
        ]


class PokemonSpeciesGender(Resource):
    pokemon_species: MinimalResource["PokemonSpecies"]
    rate: int

    def __init__(self, *, pokemon_species: Dict[str, Any], rate: int) -> None:
        self.pokemon_species = MinimalResource(**pokemon_species)
        self.rate = rate
