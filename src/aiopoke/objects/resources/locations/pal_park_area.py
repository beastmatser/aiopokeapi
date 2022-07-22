from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import PokemonSpecies


class PalParkArea(NamedResource):
    pokemon_encounters: List["PalParkEncounterSpecies"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        pokemon_encounters: List[Dict[str, Any]],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.pokemon_encounters = [
            PalParkEncounterSpecies(**pokemon_encounters)
            for pokemon_encounters in pokemon_encounters
        ]
        self.names = [Name(**name) for name in names]


class PalParkEncounterSpecies(Resource):
    base_score: int
    rate: int
    pokemon_species: MinimalResource["PokemonSpecies"]

    def __init__(
        self, base_score: int, rate: int, pokemon_species: Dict[str, Any]
    ) -> None:
        self.base_score = base_score
        self.rate = rate
        self.pokemon_species = MinimalResource(**pokemon_species)
