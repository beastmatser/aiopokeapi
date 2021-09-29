from typing import List
from ...minimal_resources import (
    MinimalGeneration,
    MinimalLanguage,
    MinimalPokedex,
    MinimalParkPalArea,
    MinimalPokemon,
    MinimalPokemonColor,
    MinimalEggGroup,
    MinimalPokemonSpecies,
    MinimalGrowthRate,
    MinimalPokemonHabitat,
    MinimalPokemonShape,
    Url
)
from ...utility.common_models import Name, NamedResource, FlavorText, Description


class PokemonSpecies(NamedResource):
    base_happiness: int
    capture_rate: int
    color: "MinimalPokemonColor"
    egg_groups: List["MinimalEggGroup"]
    evolution_chain: Url
    flavor_text_entry: FlavorText
    flavor_text_entries: List["FlavorText"]
    form_description: str
    form_descriptions: List["Description"]
    forms_switchable: bool
    gender_rate: int
    genus: "Genus"
    genera: List["Genus"]
    generation: "MinimalGeneration"
    growth_rate: "MinimalGrowthRate"
    habitat: "MinimalPokemonHabitat"
    has_gender_differences: bool
    hatch_counter: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    order: int
    names: List["Name"]
    pal_park_encounters: List["PalParkEncounterArea"]
    pokedex_numbers: List["PokemonSpeciesDexEntry"]
    shape: "MinimalPokemonShape"
    varieties: List["PokemonSpeciesVariety"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.base_happiness = data["base_happiness"]
        self.capture_rate = data["capture_rate"]
        self.color = MinimalPokemonColor(data["color"])
        self.egg_groups = [MinimalEggGroup(egg_group_data) for egg_group_data in data["egg_groups"]]
        self.evolution_chain = Url(data["evolution_chain"])
        self.evolves_from_species = MinimalPokemonSpecies(data["evolves_from_species"])
        self.flavor_text_entry = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        ][0]
        self.flavor_text_entries = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.form_description = [
            description_data["description"]
            for description_data in data["form_descriptions"]
            if description_data["language"]["name"] == "en"
        ][0]
        self.form_descriptions = [Description(description_data) for description_data in data["form_descriptions"]]
        self.forms_switchable = data["forms_switchable"]
        self.gender_rate = data["gender_rate"]
        self.genus = [Genus(genera_data) for genera_data in data["genera"] if genera_data["language"]["name"] == "en"][0]
        self.genera = [Genus(genera_data) for genera_data in data["genera"]]
        self.generation = MinimalGeneration(data["generation"])
        self.growth_rate = MinimalGrowthRate(data["growth_rate"])
        self.habitat = MinimalPokemonHabitat(data["habitat"])
        self.has_gender_differences = data["has_gender_differences"]
        self.hatch_counter = data["hatch_counter"]
        self.is_baby = data["is_baby"]
        self.is_legendary = data["is_legendary"]
        self.is_mythical = data["is_mythical"]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.order = data["order"]
        self.pal_park_encounters = [PalParkEncounterArea(pal_park_encounter_data) for pal_park_encounter_data in data["pal_park_encounters"]]
        self.pokedex_numbers = [PokemonSpeciesDexEntry(pokedex_number_data) for pokedex_number_data in data["pokedex_numbers"]]
        self.shape = MinimalPokemonShape(data["shape"])
        self.varieties = [PokemonSpeciesVariety(variety_data) for variety_data in data["varieties"]]

    def __repr__(self) -> str:
        return (
            f"<PokemonSpecies base_happiness={self.base_happiness} capture_rate={self.capture_rate} color={self.color} egg_groups={self.egg_groups} "
            f"evolution_chain={self.evolution_chain} flavor_text_entry={self.flavor_text_entry} flavor_text_entries={self.flavor_text_entries} "
            f"form_description='{self.form_description}' form_descriptions={self.form_descriptions} forms_switchable={self.forms_switchable} "
            f"gender_rate={self.gender_rate} genus={self.genus} genera={self.genera} generation={self.generation} "
            f"growth_rate={self.growth_rate} habitat={self.habitat} has_gender_differences={self.has_gender_differences} "
            f"hatch_counter={self.hatch_counter} id_={self.id_} is_baby={self.is_baby} is_legendary={self.is_legendary} is_mythical={self.is_mythical} "
            f"order={self.order} name='{self.name}' names={self.names} pal_park_encounters={self.pal_park_encounters} "
            f"pokedex_numbers={self.pokedex_numbers} shape={self.shape} varieties={self.varieties}>"
        )


class Genus:
    genus: str
    language: "MinimalLanguage"

    def __init__(self, data) -> None:
        self.genus = data["genus"]
        self.language = MinimalLanguage(data["language"])

    def __repr__(self) -> str:
        return f"<Genus genus='{self.genus}' language={self.language}>"


class PokemonSpeciesDexEntry:
    entry_number: int
    pokedex: "MinimalPokedex"

    def __init__(self, data) -> None:
        self.entry_number = data["entry_number"]
        self.pokedex = MinimalPokedex(data["pokedex"])

    def __repr__(self) -> str:
        return f"<PokemonSpeciesDexEntry entry_number={self.entry_number} pokedex={self.pokedex}>"


class PalParkEncounterArea:
    base_score: int
    rate: int
    area: "MinimalParkPalArea"

    def __init__(self, data) -> None:
        self.base_score = data["base_score"]
        self.rate = data["rate"]
        self.area = MinimalParkPalArea(data["area"])

    def __repr__(self) -> str:
        return f"<PalParkEncounterArea base_score={self.base_score} rate={self.rate} area={self.area}>"


class PokemonSpeciesVariety:
    is_default: bool
    pokemon: "MinimalPokemon"

    def __init__(self, data) -> None:
        self.is_default = data["is_default"]
        self.pokemon = MinimalPokemon(data["pokemon"])

    def __repr__(self) -> str:
        return f"<PokemonSpeciesVariety is_default={self.is_default} pokemon={self.pokemon}>"
