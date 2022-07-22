from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.objects.utility.language import Language
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import PokemonSpecies


class PokemonShape(NamedResource):
    awesome_names: List["AwesomeName"]
    names: List["Name"]
    pokemon_species: List[MinimalResource["PokemonSpecies"]]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        awesome_names: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.awesome_names = [
            AwesomeName(**awesome_name) for awesome_name in awesome_names
        ]
        self.names = [Name(**name) for name in names]
        self.pokemon_species = [
            MinimalResource(**pokemon_species) for pokemon_species in pokemon_species
        ]


class AwesomeName(Resource):
    awesome_name: str
    language: MinimalResource["Language"]

    def __init__(
        self,
        *,
        awesome_name: str,
        language: Dict[str, Any],
    ) -> None:
        self.awesome_name = awesome_name
        self.language = MinimalResource(**language)
