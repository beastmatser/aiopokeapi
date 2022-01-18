from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.objects.utility.language import Language
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


class PokemonShape(NamedResource):
    awesome_name: str
    names: List["Name"]
    pokemon_species: List[MinimalResource["PokemonSpecies"]]

    def __init__(
        self,
        *,
        awesome_name: str,
        names: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]],
    ) -> None:
        self.awesome_name = awesome_name
        self.names = [Name(**name) for name in names]
        self.pokemon_species = [
            MinimalResource(**pokemon_species) for pokemon_species in pokemon_species
        ]


class AwesomeName(Resource):
    awesome_name: str
    language: Language

    def __init__(
        self,
        *,
        awesome_name: str,
        language: Dict[str, Any],
    ) -> None:
        self.awesome_name = awesome_name
        self.language = Language(**language)
