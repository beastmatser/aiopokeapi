from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


class PokemonHabitat(NamedResource):
    names: List["Name"]
    pokemon_species: List[MinimalResource["PokemonSpecies"]]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        names: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.names = [Name(**name) for name in names]
        self.pokemon_species = [
            MinimalResource(**pokemon_species) for pokemon_species in pokemon_species
        ]
