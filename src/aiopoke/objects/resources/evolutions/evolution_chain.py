from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import (
        EvolutionTrigger,
        Item,
        Location,
        Move,
        NaturalGiftType,
        PokemonSpecies,
    )


class EvolutionChain(Resource):
    baby_trigger_item: Optional[MinimalResource["Item"]]
    chain: "ChainLink"
    id: int

    def __init__(
        self,
        *,
        baby_trigger_item: Optional[Dict[str, Any]],
        chain: Dict[str, Any],
        id: int,
    ) -> None:
        self.baby_trigger_item = (
            MinimalResource(**baby_trigger_item)
            if baby_trigger_item is not None
            else None
        )
        self.chain = ChainLink(**chain)
        self.id = id


class ChainLink(Resource):
    evolution_details: List["EvolutionDetail"]
    evolves_to: List["ChainLink"]
    is_baby: bool
    species: MinimalResource["PokemonSpecies"]

    def __init__(
        self,
        evolution_details: List[Dict[str, Any]],
        evolves_to: List[Dict[str, Any]],
        is_baby: bool,
        species: Dict[str, Any],
    ) -> None:
        self.evolution_details = [
            EvolutionDetail(**evolution_detail)
            for evolution_detail in evolution_details
        ]
        self.evolves_to = [ChainLink(**evolve_to) for evolve_to in evolves_to]
        self.is_baby = is_baby
        self.species = MinimalResource(**species)


class EvolutionDetail(Resource):
    base_form_id: None
    gender: Optional[int]
    held_item: Optional[MinimalResource["Item"]]
    item: Optional[MinimalResource["Item"]]
    known_move: Optional[MinimalResource["Move"]]
    known_move_type: Optional[MinimalResource["NaturalGiftType"]]
    location: Optional[MinimalResource["Location"]]
    min_affection: Optional[int]
    min_beauty: Optional[int]
    min_damage_taken: Optional[int]
    min_happiness: Optional[int]
    min_level: Optional[int]
    min_move_count: Optional[int]
    min_steps: Optional[int]
    needs_multiplayer: bool
    needs_overworld_rain: bool
    party_species: Optional[MinimalResource["PokemonSpecies"]]
    party_type: Optional[MinimalResource["NaturalGiftType"]]
    region_id: None
    relative_physical_stats: Optional[int]
    time_of_day: str
    trade_species: Optional[MinimalResource["PokemonSpecies"]]
    trigger: MinimalResource["EvolutionTrigger"]
    turn_upside_down: bool
    used_move: Optional[MinimalResource["Move"]]

    def __init__(
        self,
        *,
        base_form_id: None,
        gender: Optional[int],
        held_item: Optional[Dict[str, Any]],
        item: Optional[Dict[str, Any]],
        known_move: Optional[Dict[str, Any]],
        known_move_type: Optional[Dict[str, Any]],
        location: Optional[Dict[str, Any]],
        min_affection: Optional[int],
        min_beauty: Optional[int],
        min_damage_taken: Optional[int],
        min_happiness: Optional[int],
        min_level: Optional[int],
        min_move_count: Optional[int],
        min_steps: Optional[int],
        needs_multiplayer: bool,
        needs_overworld_rain: bool,
        party_species: Optional[Dict[str, Any]],
        party_type: Optional[Dict[str, Any]],
        region_id: None,
        relative_physical_stats: Optional[int],
        time_of_day: str,
        trade_species: Optional[Dict[str, Any]],
        trigger: Dict[str, Any],
        turn_upside_down: bool,
        used_move: Optional[Dict[str, Any]],
    ):
        self.base_form_id = base_form_id
        self.gender = gender
        self.held_item = MinimalResource(**held_item) if held_item is not None else None
        self.item = MinimalResource(**item) if item is not None else None
        self.known_move = (
            MinimalResource(**known_move) if known_move is not None else None
        )
        self.known_move_type = (
            MinimalResource(**known_move_type) if known_move_type is not None else None
        )
        self.location = MinimalResource(**location) if location is not None else None
        self.min_affection = min_affection
        self.min_beauty = min_beauty
        self.min_damage_taken = min_damage_taken
        self.min_happiness = min_happiness
        self.min_level = min_level
        self.min_move_count = min_move_count
        self.min_steps = min_steps
        self.needs_multiplayer = needs_multiplayer
        self.needs_overworld_rain = needs_overworld_rain
        self.party_species = (
            MinimalResource(**party_species) if party_species is not None else None
        )
        self.party_type = (
            MinimalResource(**party_type) if party_type is not None else None
        )
        self.region_id = region_id
        self.relative_physical_stats = relative_physical_stats
        self.time_of_day = time_of_day
        self.trade_species = (
            MinimalResource(**trade_species) if trade_species is not None else None
        )
        self.trigger = MinimalResource(**trigger)
        self.turn_upside_down = turn_upside_down
        self.used_move = MinimalResource(**used_move) if used_move is not None else None
