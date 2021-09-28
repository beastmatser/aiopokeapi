from typing import List
from ...minimal_resources import MinimalPokemonSpecies
from ...utility import NamedResource


class Gender(NamedResource):
    pokemon_species_details: List["PokemonSpeciesGender"]
    required_for_evolution: List["MinimalPokemonSpecies"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.pokemon_species_details = [
            PokemonSpeciesGender(pokemon_species_detail_data)
            for pokemon_species_detail_data in data["pokemon_species_details"]
        ]
        self.required_for_evolution = [
            MinimalPokemonSpecies(pokemon_species_data)
            for pokemon_species_data in data["required_for_evolution"]
        ]

    def __repr__(self) -> str:
        return (
            f"<Gender id_={self.id_} name={self.name} pokemon_species_details={self.pokemon_species_details} "
            f"required_for_evolution={self.required_for_evolution}>"
        )


class PokemonSpeciesGender:
    pokemon_species: "MinimalPokemonSpecies"
    rate: int

    def __init__(self, data) -> None:
        self.pokemon_species = MinimalPokemonSpecies(data["pokemon_species"])
        self.rate = data["rate"]

    def __repr__(self) -> str:
        return f"<PokemonSpeciesGender pokemon_species={self.pokemon_species} rate={self.rate}>"
