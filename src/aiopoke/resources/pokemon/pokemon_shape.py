from typing import List
from ...minimal_resources import MinimalPokemonSpecies
from ...utility.common_models import Name, NamedResource


class PokemonShape(NamedResource):
    awesome_name: str
    names: List["Name"]
    pokemon_species: List["MinimalPokemonSpecies"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.awesome_name = [
            awesome_name_data["awesome_name"]
            for awesome_name_data in data["awesome_names"]
            if awesome_name_data["language"]["name"] == "en"
        ][0]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.pokemon_species = [
            MinimalPokemonSpecies(pokemon_species_data)
            for pokemon_species_data in data["pokemon_species"]
        ]

    def __repr__(self) -> str:
        return f"<PokemonColor awesome_name='{self.awesome_name}' id_={self.id_} name='{self.name}' names={self.names} pokemon_species={self.pokemon_species}>"
