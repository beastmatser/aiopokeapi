from typing import TYPE_CHECKING, List, Any, Dict

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import PokemonSpecies


class EvolutionTrigger(NamedResource):
    pokemon_species: List[MinimalResource["PokemonSpecies"]]
    names: List["Name"]

    def __init__(
        self, pokemon_species: List[Dict[str, Any]], names: List[Dict[str, Any]]
    ) -> None:
        self.pokemon_species = [
            MinimalResource(**pokemon_species) for pokemon_species in pokemon_species
        ]
        self.names = [Name(**name) for name in names]
