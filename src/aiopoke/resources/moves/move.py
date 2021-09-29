from typing import List, Optional

from ...minimal_resources import (
    ContestEffectUrl,
    MinimalContestType,
    MinimalGeneration,
    MinimalLanguage,
    MinimalMove,
    MinimalMoveAilment,
    MinimalMoveCategory,
    MinimalMoveDamageClass,
    MinimalNaturalGiftType,
    MinimalPokemon,
    MinimalStat,
    MinimalVersionGroup,
)
from ...utility.common_models import (
    MachineVersionDetail,
    Name,
    NamedResource,
    VerboseEffect,
)
from ..pokemon.ability import AbilityEffectChange


class Move(NamedResource):
    accuracy: int
    contest_combos: "ContestComboSets"
    contest_effect: ContestEffectUrl
    contest_type: "MinimalContestType"
    damage_class: "MinimalMoveDamageClass"
    effect_chance: Optional[int]
    effect_entry: "VerboseEffect"
    effect_entries: List["VerboseEffect"]
    flavor_text_entry: "MoveFlavorText"
    flavor_text_entries: List["MoveFlavorText"]
    generation: "MinimalGeneration"
    learned_by_pokemon: List["MinimalPokemon"]
    machines: List["MachineVersionDetail"]
    meta: "MoveMetaData"
    names: List["Name"]
    past_values: List["PastMoveStatValues"]
    power: int
    pp: int
    priority: int
    stat_changes: List["MoveStatChange"]
    type_: "MinimalNaturalGiftType"

    def __init__(self, data) -> None:
        super().__init__(data)
        self.accuracy = data["accuracy"]
        self.contest_combos = ContestComboSets(data["contest_combos"])
        self.contest_effect = ContestEffectUrl(data["contest_effect"])
        self.contest_type = MinimalContestType(data["contest_type"])
        self.damage_class = MinimalMoveDamageClass(data["damage_class"])
        self.effect_chance = data["effect_chance"]
        self.effect_changes = [
            AbilityEffectChange(effect_change_data)
            for effect_change_data in data["effect_changes"]
        ]
        self.effect_entry = [
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        ][0]
        self.effect_entries = [
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        ]
        self.flavor_text_entry = [
            MoveFlavorText(move_flavor_text_entry_data)
            for move_flavor_text_entry_data in data["flavor_text_entries"]
            if move_flavor_text_entry_data["language"]["name"] == "en"
        ][0]
        self.flavor_text_entries = [
            MoveFlavorText(move_flavor_text_entry_data)
            for move_flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.generation = MinimalGeneration(data["generation"])
        self.learned_by_pokemon = [
            MinimalPokemon(pokemon_data) for pokemon_data in data["learned_by_pokemon"]
        ]
        self.machines = [
            MachineVersionDetail(machine_data) for machine_data in data["machines"]
        ]
        self.meta = MoveMetaData(data["meta"])
        self.names = [Name(name_data) for name_data in data["names"]]
        self.past_values = [
            PastMoveStatValues(past_value_data)
            for past_value_data in data["past_values"]
        ]
        self.power = data["power"]
        self.pp = data["pp"]
        self.priority = data["priority"]
        self.stat_changes = [
            MoveStatChange(stat_change_data)
            for stat_change_data in data["stat_changes"]
        ]
        self.type_ = MinimalNaturalGiftType(data["type"])

    def __repr__(self) -> str:
        return (
            f"<Move accuracy={self.accuracy} contest_combos={self.contest_combos} contest_effect={self.contest_effect} contest_type={self.contest_type} "
            f"damage_class={self.damage_class} effect_chance={self.effect_chance} effect_entry={self.effect_entry} effect_entries={self.effect_entries} "
            f"flavor_text_entry={self.flavor_text_entry} flavor_text_entries={self.flavor_text_entries} generation={self.generation} id_={self.id_} "
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
    use_before: List["MinimalMove"]
    use_after: List["MinimalMove"]

    def __init__(self, data) -> None:
        self.use_before = [MinimalMove(move_data) for move_data in data["use_before"]]
        self.use_after = [MinimalMove(move_data) for move_data in data["use_after"]]

    def __repr__(self) -> str:
        return f"<ContestComboDetail use_before={self.use_before} use_after={self.use_after}>"


class MoveFlavorText:
    flavor_text: str
    language: "MinimalLanguage"
    version_group: "MinimalVersionGroup"

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalLanguage(data["language"])
        self.version_group = MinimalVersionGroup(data["version_group"])

    def __repr__(self) -> str:
        return f"<MoveFlavorText flavor_text='{self.flavor_text}' language={self.language} version_group={self.version_group}>"


class MoveMetaData:
    ailment: "MinimalMoveAilment"
    category: "MinimalMoveCategory"
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
        self.ailment = MinimalMoveAilment(data["ailment"])
        self.category = MinimalMoveCategory(data["category"])
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
    stat: "MinimalStat"

    def __init__(self, data) -> None:
        self.change = data["change"]
        self.stat = MinimalStat(data["stat"])

    def __repr__(self) -> str:
        return f"<MoveStatChange change={self.change} stat={self.stat}>"


class PastMoveStatValues:
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entry: "VerboseEffect"
    effect_entries: List["VerboseEffect"]
    type_: "MinimalNaturalGiftType"

    def __init__(self, data) -> None:
        self.accuracy = data["accuracy"]
        self.effect_chance = data["effect_chance"]
        self.power = data["power"]
        self.pp = data["pp"]
        self.effect_entry = [
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        ][0]
        self.effect_entries = [
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        ]
        self.type_ = MinimalNaturalGiftType(data["type"])
        self.version_group = MinimalVersionGroup(data["version_group"])

    def __repr__(self) -> str:
        return (
            f"<PastMoveStatValues accuracy={self.accuracy} effect_chance={self.effect_chance} power={self.power} pp={self.pp} "
            f"effect_entry={self.effect_entry} effect_entries={self.effect_entries} type_={self.type_}>"
        )
