from typing import Tuple, TYPE_CHECKING
from ...minimal_resources import MinimalResource, Url
from ...utility import Name, NamedResource, FlavorText, Description

if TYPE_CHECKING:
    from . import GrowthRate, EggGroup, Pokemon, PokemonHabitat, PokemonShape, PokemonColor
    from ...resources import (
        EvolutionChain,
        Generation,
        Pokedex,
        PalParkArea
    )
    from ...utility import Language


class PokemonSpecies(NamedResource):
    base_happiness: int
    capture_rate: int
    color: MinimalResource["PokemonColor"]
    egg_groups: Tuple[MinimalResource["EggGroup"], ...]
    evolution_chain: Url["EvolutionChain"]
    evolves_from_species: MinimalResource["PokemonSpecies"]
    flavor_text_entry: "FlavorText"
    flavor_text_entries: Tuple["FlavorText", ...]
    form_description: str
    form_descriptions: Tuple["Description", ...]
    forms_switchable: bool
    gender_rate: int
    genus: "Genus"
    genera: Tuple["Genus", ...]
    generation: MinimalResource["Generation"]
    growth_rate: MinimalResource["GrowthRate"]
    habitat: MinimalResource["PokemonHabitat"]
    has_gender_differences: bool
    hatch_counter: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    order: int
    names: Tuple["Name", ...]
    pal_park_encounters: Tuple["PalParkEncounterArea", ...]
    pokedex_numbers: Tuple["PokemonSpeciesDexEntry", ...]
    shape: MinimalResource["PokemonShape"]
    varieties: Tuple["PokemonSpeciesVariety", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.base_happiness = data["base_happiness"]
        self.capture_rate = data["capture_rate"]
        self.color = MinimalResource(data["color"])
        self.egg_groups = tuple(MinimalResource(egg_group_data) for egg_group_data in data["egg_groups"])
        self.evolution_chain = Url(data["evolution_chain"])
        self.evolves_from_species = MinimalResource(data["evolves_from_species"])
        self.flavor_text_entry = tuple(
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        )[0]
        self.flavor_text_entries = tuple(
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        )
        self.form_description = tuple(
            description_data["description"]
            for description_data in data["form_descriptions"]
            if description_data["language"]["name"] == "en"
        )[0]
        self.form_descriptions = tuple(Description(description_data) for description_data in data["form_descriptions"])
        self.forms_switchable = data["forms_switchable"]
        self.gender_rate = data["gender_rate"]
        self.genus = tuple(Genus(genera_data) for genera_data in data["genera"] if genera_data["language"]["name"] == "en")[0]
        self.genera = tuple(Genus(genera_data) for genera_data in data["genera"])
        self.generation = MinimalResource(data["generation"])
        self.growth_rate = MinimalResource(data["growth_rate"])
        self.habitat = MinimalResource(data["habitat"])
        self.has_gender_differences = data["has_gender_differences"]
        self.hatch_counter = data["hatch_counter"]
        self.is_baby = data["is_baby"]
        self.is_legendary = data["is_legendary"]
        self.is_mythical = data["is_mythical"]
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.order = data["order"]
        self.pal_park_encounters = tuple(PalParkEncounterArea(pal_park_encounter_data) for pal_park_encounter_data in data["pal_park_encounters"])
        self.pokedex_numbers = tuple(PokemonSpeciesDexEntry(pokedex_number_data) for pokedex_number_data in data["pokedex_numbers"])
        self.shape = MinimalResource(data["shape"])
        self.varieties = tuple(PokemonSpeciesVariety(variety_data) for variety_data in data["varieties"])

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
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.genus = data["genus"]
        self.language = MinimalResource(data["language"])

    def __repr__(self) -> str:
        return f"<Genus genus='{self.genus}' language={self.language}>"


class PokemonSpeciesDexEntry:
    entry_number: int
    pokedex: MinimalResource["Pokedex"]

    def __init__(self, data) -> None:
        self.entry_number = data["entry_number"]
        self.pokedex = MinimalResource(data["pokedex"])

    def __repr__(self) -> str:
        return f"<PokemonSpeciesDexEntry entry_number={self.entry_number} pokedex={self.pokedex}>"


class PalParkEncounterArea:
    base_score: int
    rate: int
    area: MinimalResource["PalParkArea"]

    def __init__(self, data) -> None:
        self.base_score = data["base_score"]
        self.rate = data["rate"]
        self.area = MinimalResource(data["area"])

    def __repr__(self) -> str:
        return f"<PalParkEncounterArea base_score={self.base_score} rate={self.rate} area={self.area}>"


class PokemonSpeciesVariety:
    is_default: bool
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, data) -> None:
        self.is_default = data["is_default"]
        self.pokemon = MinimalResource(data["pokemon"])

    def __repr__(self) -> str:
        return f"<PokemonSpeciesVariety is_default={self.is_default} pokemon={self.pokemon}>"
