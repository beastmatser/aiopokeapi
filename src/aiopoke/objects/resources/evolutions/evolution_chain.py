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
        baby_trigger_item: Dict[str, Any],
        chain: Dict[str, Any],
        id: int,
    ) -> None:
        self.baby_trigger_item = MinimalResource(**baby_trigger_item)
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
    gender: Optional[int]
    held_item: Optional[MinimalResource["Item"]]
    item: Optional[MinimalResource["Item"]]
    known_move: Optional[MinimalResource["Move"]]
    known_move_type: Optional[MinimalResource["NaturalGiftType"]]
    location: Optional[MinimalResource["Location"]]
    min_affection: Optional[int]
    min_beauty: Optional[int]
    min_happiness: Optional[int]
    min_level: int
    needs_overworld_rain: Optional[bool]
    party_species: Optional[MinimalResource["PokemonSpecies"]]
    party_type: Optional[MinimalResource["NaturalGiftType"]]
    relative_physical_stats: Optional[int]
    time_of_day: str
    trade_species: Optional[MinimalResource["PokemonSpecies"]]
    trigger: MinimalResource["EvolutionTrigger"]
    turn_upside_down: bool

    def __init__(
        self,
        *,
        gender: Optional[int],
        held_item: Dict[str, Any],
        item: Dict[str, Any],
        known_move: Dict[str, Any],
        known_move_type: Dict[str, Any],
        location: Dict[str, Any],
        min_affection: Optional[int],
        min_beauty: Optional[int],
        min_happiness: Optional[int],
        min_level: int,
        needs_overworld_rain: Optional[bool],
        party_species: Dict[str, Any],
        party_type: Dict[str, Any],
        relative_physical_stats: Optional[int],
        time_of_day: str,
        trade_species: Dict[str, Any],
        trigger: Dict[str, Any],
        turn_upside_down: bool,
    ):
        self.gender = gender
        self.held_item = MinimalResource(**held_item)
        self.item = MinimalResource(**item)
        self.known_move = MinimalResource(**known_move)
        self.known_move_type = MinimalResource(**known_move_type)
        self.location = MinimalResource(**location)
        self.min_affection = min_affection
        self.min_beauty = min_beauty
        self.min_happiness = min_happiness
        self.min_level = min_level
        self.needs_overworld_rain = needs_overworld_rain
        self.party_species = MinimalResource(**party_species)
        self.party_type = MinimalResource(**party_type)
        self.relative_physical_stats = relative_physical_stats
        self.time_of_day = time_of_day
        self.trade_species = MinimalResource(**trade_species)
        self.trigger = MinimalResource(**trigger)
        self.turn_upside_down = turn_upside_down
