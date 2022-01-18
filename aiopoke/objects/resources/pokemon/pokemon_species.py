from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Description
from aiopoke.objects.utility import FlavorText
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.minimal_resources import Url

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import (
        GrowthRate,
        EggGroup,
        Pokemon,
        PokemonHabitat,
        PokemonShape,
        PokemonColor,
    )
    from aiopoke.objects.resources import (
        EvolutionChain,
        Generation,
        Pokedex,
        PalParkArea,
    )
    from aiopoke.objects.utility import Language


class PokemonSpecies(NamedResource):
    base_happiness: int
    capture_rate: int
    color: MinimalResource["PokemonColor"]
    egg_groups: List[MinimalResource["EggGroup"]]
    evolution_chain: Url["EvolutionChain"]
    evolves_from_species: MinimalResource["PokemonSpecies"]
    flavor_text_entries: List["FlavorText"]
    form_descriptions: List["Description"]
    forms_switchable: bool
    gender_rate: int
    genera: List["Genus"]
    generation: MinimalResource["Generation"]
    growth_rate: MinimalResource["GrowthRate"]
    habitat: MinimalResource["PokemonHabitat"]
    has_gender_differences: bool
    hatch_counter: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    order: int
    names: List["Name"]
    pal_park_encounters: List["PalParkEncounterArea"]
    pokedex_numbers: List["PokemonSpeciesDexEntry"]
    shape: MinimalResource["PokemonShape"]
    varieties: List["PokemonSpeciesVariety"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.base_happiness = data["base_happiness"]
        self.capture_rate = data["capture_rate"]
        self.color = MinimalResource(data["color"])
        self.egg_groups = [
            MinimalResource(egg_group_data) for egg_group_data in data["egg_groups"]
        ]
        self.evolution_chain = Url(data["evolution_chain"])
        self.evolves_from_species = MinimalResource(data["evolves_from_species"])
        self.flavor_text_entries = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.form_descriptions = [
            Description(description_data)
            for description_data in data["form_descriptions"]
        ]
        self.forms_switchable = data["forms_switchable"]
        self.gender_rate = data["gender_rate"]
        self.genera = [Genus(genera_data) for genera_data in data["genera"]]
        self.generation = MinimalResource(data["generation"])
        self.growth_rate = MinimalResource(data["growth_rate"])
        self.habitat = MinimalResource(data["habitat"])
        self.has_gender_differences = data["has_gender_differences"]
        self.hatch_counter = data["hatch_counter"]
        self.is_baby = data["is_baby"]
        self.is_legendary = data["is_legendary"]
        self.is_mythical = data["is_mythical"]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.order = data["order"]
        self.pal_park_encounters = [
            PalParkEncounterArea(pal_park_encounter_data)
            for pal_park_encounter_data in data["pal_park_encounters"]
        ]
        self.pokedex_numbers = [
            PokemonSpeciesDexEntry(pokedex_number_data)
            for pokedex_number_data in data["pokedex_numbers"]
        ]
        self.shape = MinimalResource(data["shape"])
        self.varieties = [
            PokemonSpeciesVariety(variety_data) for variety_data in data["varieties"]
        ]


class Genus(Resource):
    genus: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.genus = data["genus"]
        self.language = MinimalResource(data["language"])


class PokemonSpeciesDexEntry(Resource):
    entry_number: int
    pokedex: MinimalResource["Pokedex"]

    def __init__(self, data) -> None:
        self.entry_number = data["entry_number"]
        self.pokedex = MinimalResource(data["pokedex"])


class PalParkEncounterArea(Resource):
    base_score: int
    rate: int
    area: MinimalResource["PalParkArea"]

    def __init__(self, data) -> None:
        self.base_score = data["base_score"]
        self.rate = data["rate"]
        self.area = MinimalResource(data["area"])


class PokemonSpeciesVariety(Resource):
    is_default: bool
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, data) -> None:
        self.is_default = data["is_default"]
        self.pokemon = MinimalResource(data["pokemon"])
