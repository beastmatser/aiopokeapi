from typing import TYPE_CHECKING, Optional, Tuple

from ...minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...resources import (
        EvolutionTrigger,
        Item,
        Location,
        Move,
        NaturalGiftType,
        PokemonSpecies,
    )


class EvolutionChain:
    baby_trigger_item: Optional[MinimalResource["Item"]]
    chain: "ChainLink"
    id_: int

    def __init__(self, data) -> None:
        self.baby_trigger_item = (
            MinimalResource(data["baby_trigger_item"])
            if data.get("baby_trigger_item") is not None
            else None
        )
        self.chain = ChainLink(data["chain"])
        self.id_ = data["id"]

    def __repr__(self) -> str:
        return f"<EvolutionChain baby_trigger_item={self.baby_trigger_item} chain={self.chain} id_={self.id_}>"


class ChainLink:
    evolution_details: Tuple["EvolutionDetail", ...]
    evolves_to: Tuple["ChainLink", ...]
    is_baby: bool
    species: MinimalResource["PokemonSpecies"]

    def __init__(self, data) -> None:
        self.evolution_details = tuple(
            EvolutionDetail(evolution_detail_data)
            for evolution_detail_data in data["evolution_details"]
        )
        self.evolves_to = tuple(
            ChainLink(evolves_to_data) for evolves_to_data in data["evolves_to"]
        )
        self.is_baby = data["is_baby"]
        self.species = MinimalResource(data["species"])

    def __repr__(self) -> str:
        return f"<ChainLink evolution_details={self.evolution_details} evolves_to={self.evolves_to} is_baby={self.is_baby} species={self.species}>"


class EvolutionDetail:
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

    def __init__(self, data) -> None:
        self.gender = data["gender"]
        self.held_item = (
            MinimalResource(data["held_item"])
            if data.get("held_item") is not None
            else None
        )
        self.item = (
            MinimalResource(data["item"]) if data.get("item") is not None else None
        )
        self.known_move = (
            MinimalResource(data["known_move"])
            if data.get("known_move") is not None
            else None
        )
        self.known_move_type = (
            MinimalResource(data["known_move_type"])
            if data.get("known_move_type") is not None
            else None
        )
        self.location = (
            MinimalResource(data["location"])
            if data.get("location") is not None
            else None
        )
        self.min_affection = data["min_affection"]
        self.min_beauty = data["min_beauty"]
        self.min_happiness = data["min_happiness"]
        self.min_level = data["min_level"]
        self.needs_overworld_rain = data["needs_overworld_rain"]
        self.party_species = (
            MinimalResource(data["party_species"])
            if data.get("party_species") is not None
            else None
        )
        self.party_type = (
            MinimalResource(data["party_type"])
            if data.get("party_type") is not None
            else None
        )
        self.relative_physical_stats = data["relative_physical_stats"]
        self.time_of_day = data["time_of_day"]
        self.trade_species = (
            MinimalResource(data["trade_species"])
            if data.get("trade_species") is not None
            else None
        )
        self.trigger = MinimalResource(data["trigger"])
        self.turn_upside_down = data["turn_upside_down"]

    def __repr__(self) -> str:
        return (
            f"<EvolutionDetail gender={self.gender} held_item={self.held_item} item={self.item} known_move={self.known_move} "
            f"known_move_type={self.known_move_type} location={self.location} min_affection={self.min_affection} "
            f"min_beauty={self.min_beauty} min_happiness={self.min_happiness} min_level={self.min_level} "
            f"needs_overworld_rain={self.needs_overworld_rain} party_species={self.party_species} party_type={self.party_type} "
            f"relative_physical_stats={self.relative_physical_stats} time_of_day='{self.time_of_day}' trade_species={self.trade_species} "
            f"trigger={self.trigger} turn_upside_down={self.turn_upside_down}>"
        )
