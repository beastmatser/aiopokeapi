from typing import TYPE_CHECKING, Any, Dict, List, Optional

from aiopoke.objects.utility import Description, FlavorText, Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource, Url
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import (
        EvolutionChain,
        Generation,
        PalParkArea,
        Pokedex,
    )
    from aiopoke.objects.resources.pokemon import (
        EggGroup,
        GrowthRate,
        Pokemon,
        PokemonColor,
        PokemonHabitat,
        PokemonShape,
    )
    from aiopoke.objects.utility import Language


class PokemonSpecies(NamedResource):
    base_happiness: int
    capture_rate: int
    color: MinimalResource["PokemonColor"]
    egg_groups: List[MinimalResource["EggGroup"]]
    evolution_chain: Url["EvolutionChain"]
    evolves_from_species: Optional[MinimalResource["PokemonSpecies"]]
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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        base_happiness: int,
        capture_rate: int,
        color: Dict[str, Any],
        egg_groups: List[Dict[str, Any]],
        evolution_chain: Dict[str, Any],
        evolves_from_species: Optional[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
        form_descriptions: List[Dict[str, Any]],
        forms_switchable: bool,
        gender_rate: int,
        genera: List[Dict[str, Any]],
        generation: Dict[str, Any],
        growth_rate: Dict[str, Any],
        habitat: Dict[str, Any],
        has_gender_differences: bool,
        hatch_counter: int,
        is_baby: bool,
        is_legendary: bool,
        is_mythical: bool,
        order: int,
        names: List[Dict[str, Any]],
        pal_park_encounters: List[Dict[str, Any]],
        pokedex_numbers: List[Dict[str, Any]],
        shape: Dict[str, Any],
        varieties: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.base_happiness = base_happiness
        self.capture_rate = capture_rate
        self.color = MinimalResource(**color)
        self.egg_groups = [MinimalResource(**egg_group) for egg_group in egg_groups]
        self.evolution_chain = Url(**evolution_chain)
        self.evolves_from_species = (
            MinimalResource(**evolves_from_species)
            if evolves_from_species is not None
            else None
        )
        self.flavor_text_entries = [
            FlavorText(**flavor_text_entry) for flavor_text_entry in flavor_text_entries
        ]
        self.form_descriptions = [
            Description(**form_description) for form_description in form_descriptions
        ]
        self.forms_switchable = forms_switchable
        self.gender_rate = gender_rate
        self.genera = [Genus(**genus_data) for genus_data in genera]
        self.generation = MinimalResource(**generation)
        self.growth_rate = MinimalResource(**growth_rate)
        self.habitat = MinimalResource(**habitat)
        self.has_gender_differences = has_gender_differences
        self.hatch_counter = hatch_counter
        self.is_baby = is_baby
        self.is_legendary = is_legendary
        self.is_mythical = is_mythical
        self.order = order
        self.names = [Name(**name) for name in names]
        self.pal_park_encounters = [
            PalParkEncounterArea(**pal_park_encounter)
            for pal_park_encounter in pal_park_encounters
        ]
        self.pokedex_numbers = [
            PokemonSpeciesDexEntry(**pokedex_number)
            for pokedex_number in pokedex_numbers
        ]
        self.shape = MinimalResource(**shape)
        self.varieties = [PokemonSpeciesVariety(**variety) for variety in varieties]


class Genus(Resource):
    genus: str
    language: MinimalResource["Language"]

    def __init__(self, genus: str, language: Dict[str, Any]) -> None:
        self.genus = genus
        self.language = MinimalResource(**language)


class PokemonSpeciesDexEntry(Resource):
    entry_number: int
    pokedex: MinimalResource["Pokedex"]

    def __init__(self, *, entry_number: int, pokedex: Dict[str, Any]) -> None:
        self.entry_number = entry_number
        self.pokedex = MinimalResource(**pokedex)


class PalParkEncounterArea(Resource):
    base_score: int
    rate: int
    area: MinimalResource["PalParkArea"]

    def __init__(self, *, base_score: int, rate: int, area: Dict[str, Any]) -> None:
        self.base_score = base_score
        self.rate = rate
        self.area = MinimalResource(**area)


class PokemonSpeciesVariety(Resource):
    is_default: bool
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, *, is_default: bool, pokemon: Dict[str, Any]) -> None:
        self.is_default = is_default
        self.pokemon = MinimalResource(**pokemon)
