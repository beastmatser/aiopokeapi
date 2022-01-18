from typing import TYPE_CHECKING, List

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

    def __init__(self, data) -> None:
        super().__init__(data)
        self.awesome_names = [
            AwesomeName(awesome_name_data)
            for awesome_name_data in data["awesome_names"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.pokemon_species = [
            MinimalResource(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        ]


class AwesomeName(Resource):
    awesome_name: str
    language: Language

    def __init__(self, data) -> None:
        self.awesome_name = data["awesome_name"]
        self.language = Language(data["language"])
