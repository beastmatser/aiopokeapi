from typing import Optional
from typing import Tuple
from typing import TYPE_CHECKING

from ...minimal_resources import MinimalResource
from ...minimal_resources import Url
from ...utility import MachineVersionDetail
from ...utility import Name
from ...utility import NamedResource
from ...utility import VerboseEffect
from ..pokemon.ability import AbilityEffectChange

if TYPE_CHECKING:
    from ...resources import (
        ContestEffect,
        ContestType,
        Generation,
        NaturalGiftType,
        Pokemon,
        Stat,
        VersionGroup,
    )
    from ...utility import Language
    from . import MoveAilment, MoveCategory, MoveDamageClass


class Move(NamedResource):
    accuracy: int
    contest_combos: "ContestComboSets"
    contest_effect: Url["ContestEffect"]
    contest_type: MinimalResource["ContestType"]
    damage_class: MinimalResource["MoveDamageClass"]
    effect_chance: Optional[int]
    effect_entry: "VerboseEffect"
    effect_entries: Tuple["VerboseEffect", ...]
    flavor_text_entry: "MoveFlavorText"
    flavor_text_entries: Tuple["MoveFlavorText", ...]
    generation: MinimalResource["Generation"]
    learned_by_pokemon: Tuple[MinimalResource["Pokemon"], ...]
    machines: Tuple["MachineVersionDetail", ...]
    meta: "MoveMetaData"
    names: Tuple["Name", ...]
    past_values: Tuple["PastMoveStatValues", ...]
    power: int
    pp: int
    priority: int
    stat_changes: Tuple["MoveStatChange", ...]
    type_: MinimalResource["NaturalGiftType"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.accuracy = data["accuracy"]
        self.contest_combos = ContestComboSets(data["contest_combos"])
        self.contest_effect = Url(data["contest_effect"])
        self.contest_type = MinimalResource(data["contest_type"])
        self.damage_class = MinimalResource(data["damage_class"])
        self.effect_chance = data["effect_chance"]
        self.effect_changes = tuple(
            AbilityEffectChange(effect_change_data)
            for effect_change_data in data["effect_changes"]
        )
        self.effect_entry = tuple(
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        )[0]
        self.effect_entries = tuple(
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        )
        self.flavor_text_entry = tuple(
            MoveFlavorText(move_flavor_text_entry_data)
            for move_flavor_text_entry_data in data["flavor_text_entries"]
            if move_flavor_text_entry_data["language"]["name"] == "en"
        )[0]
        self.flavor_text_entries = tuple(
            MoveFlavorText(move_flavor_text_entry_data)
            for move_flavor_text_entry_data in data["flavor_text_entries"]
        )
        self.generation = MinimalResource(data["generation"])
        self.learned_by_pokemon = tuple(
            MinimalResource(pokemon_data) for pokemon_data in data["learned_by_pokemon"]
        )
        self.machines = tuple(
            MachineVersionDetail(machine_data) for machine_data in data["machines"]
        )
        self.meta = MoveMetaData(data["meta"])
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.past_values = tuple(
            PastMoveStatValues(past_value_data)
            for past_value_data in data["past_values"]
        )
        self.power = data["power"]
        self.pp = data["pp"]
        self.priority = data["priority"]
        self.stat_changes = tuple(
            MoveStatChange(stat_change_data)
            for stat_change_data in data["stat_changes"]
        )
        self.type_ = MinimalResource(data["type"])

    def __repr__(self) -> str:
        return (
            f"<Move accuracy={self.accuracy} contest_combos={self.contest_combos} contest_effect={self.contest_effect} contest_type={self.contest_type} "
            f"damage_class={self.damage_class} effect_chance={self.effect_chance} effect_entry={self.effect_entry} effect_entries={self.effect_entries} "
            f"flavor_text_entry={self.flavor_text_entry} flavor_text_entries={self.flavor_text_entries} generation={self.generation} id_={self.id} "
            f"learned_by_pokemon={self.learned_by_pokemon} machines={self.machines} meta={self.meta} name='{self.name}' names={self.names} "
            f"past_values={self.past_values} power={self.power} pp={self.pp} priority={self.priority} stat_changes={self.stat_changes} type_={self.type_}>"
        )


class ContestComboSets:
    normal: Optional["ContestComboDetail"]
    super: Optional["ContestComboDetail"]

    def __init__(self, data) -> None:
        self.normal = (
            ContestComboDetail(data["normal"]) if data["normal"] is not None else None
        )
        self.super = (
            ContestComboDetail(data["super"]) if data["super"] is not None else None
        )

    def __repr__(self) -> str:
        return f"<ContestComboSets normal={self.normal} super={self.super}>"


class ContestComboDetail:
    use_before: Optional[Tuple[MinimalResource["Move"], ...]]
    use_after: Optional[Tuple[MinimalResource["Move"], ...]]

    def __init__(self, data) -> None:
        self.use_before = (
            tuple(MinimalResource(move_data) for move_data in data["use_before"])
            if data["use_before"] is not None
            else None
        )
        self.use_after = (
            tuple(MinimalResource(move_data) for move_data in data["use_after"])
            if data["use_after"] is not None
            else None
        )

    def __repr__(self) -> str:
        return f"<ContestComboDetail use_before={self.use_before} use_after={self.use_after}>"


class MoveFlavorText:
    flavor_text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalResource(data["language"])
        self.version_group = MinimalResource(data["version_group"])

    def __repr__(self) -> str:
        return f"<MoveFlavorText flavor_text='{self.flavor_text}' language={self.language} version_group={self.version_group}>"


class MoveMetaData:
    ailment: MinimalResource["MoveAilment"]
    category: MinimalResource["MoveCategory"]
    min_hits: int
    max_hits: int
    min_turns: int
    max_turns: int
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int

    def __init__(self, data) -> None:
        self.ailment = MinimalResource(data["ailment"])
        self.category = MinimalResource(data["category"])
        self.min_hits = data["min_hits"]
        self.max_hits = data["max_hits"]
        self.min_turns = data["min_turns"]
        self.max_turns = data["max_turns"]
        self.drain = data["drain"]
        self.healing = data["healing"]
        self.crit_rate = data["crit_rate"]
        self.ailment_chance = data["ailment_chance"]
        self.flinch_chance = data["flinch_chance"]
        self.stat_chance = data["stat_chance"]

    def __repr__(self) -> str:
        return (
            f"<MoveMetaData ailment={self.ailment} category={self.category} min_hits={self.min_hits} max_hits={self.max_hits} "
            f"min_turns={self.min_turns} max_turns={self.max_turns} drain={self.drain} healing={self.healing} "
            f"crit_rate={self.crit_rate} ailment_chance={self.ailment_chance} flinch_chance={self.flinch_chance} stat_chance={self.stat_chance}>"
        )


class MoveStatChange:
    change: int
    stat: MinimalResource["Stat"]

    def __init__(self, data) -> None:
        self.change = data["change"]
        self.stat = MinimalResource(data["stat"])

    def __repr__(self) -> str:
        return f"<MoveStatChange change={self.change} stat={self.stat}>"


class PastMoveStatValues:
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entry: "VerboseEffect"
    effect_entries: Tuple["VerboseEffect", ...]
    type_: MinimalResource["NaturalGiftType"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.accuracy = data["accuracy"]
        self.effect_chance = data["effect_chance"]
        self.power = data["power"]
        self.pp = data["pp"]
        self.effect_entry = tuple(
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        )[0]
        self.effect_entries = tuple(
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        )
        self.type_ = MinimalResource(data["type"])
        self.version_group = MinimalResource(data["version_group"])

    def __repr__(self) -> str:
        return (
            f"<PastMoveStatValues accuracy={self.accuracy} effect_chance={self.effect_chance} power={self.power} pp={self.pp} "
            f"effect_entry={self.effect_entry} effect_entries={self.effect_entries} type_={self.type_}>"
        )
