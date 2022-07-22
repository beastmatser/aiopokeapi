from typing import TYPE_CHECKING, Any, Dict, List, Optional

from aiopoke.objects.resources.contests.super_contest_effect import SuperContestEffect
from aiopoke.objects.resources.pokemon.ability import AbilityEffectChange
from aiopoke.objects.utility import (
    MachineVersionDetail,
    Name,
    NamedResource,
    VerboseEffect,
)
from aiopoke.utils.minimal_resources import MinimalResource, Url
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import (
        ContestEffect,
        ContestType,
        Generation,
        NaturalGiftType,
        Pokemon,
        Stat,
        VersionGroup,
    )
    from aiopoke.objects.resources.moves import (
        MoveAilment,
        MoveCategory,
        MoveDamageClass,
        MoveTarget,
    )
    from aiopoke.objects.utility import Language


class Move(NamedResource):
    accuracy: int
    contest_combos: "ContestComboSets"
    contest_effect: Url["ContestEffect"]
    contest_type: MinimalResource["ContestType"]
    damage_class: MinimalResource["MoveDamageClass"]
    effect_chance: Optional[int]
    effect_changes: List["AbilityEffectChange"]
    effect_entries: List["VerboseEffect"]
    flavor_text_entries: List["MoveFlavorText"]
    generation: MinimalResource["Generation"]
    learned_by_pokemon: List[MinimalResource["Pokemon"]]
    machines: List["MachineVersionDetail"]
    meta: "MoveMetaData"
    names: List["Name"]
    past_values: List["PastMoveStatValues"]
    power: int
    pp: int
    priority: int
    stat_changes: List["MoveStatChange"]
    super_contest_effect: Url["SuperContestEffect"]
    target: MinimalResource["MoveTarget"]
    type: MinimalResource["NaturalGiftType"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        accuracy: int,
        contest_combos: Dict[str, Any],
        contest_effect: Dict[str, Any],
        contest_type: Dict[str, Any],
        damage_class: Dict[str, Any],
        effect_chance: Optional[int],
        effect_entries: List[Dict[str, Any]],
        effect_changes: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
        generation: Dict[str, Any],
        learned_by_pokemon: List[Dict[str, Any]],
        machines: List[Dict[str, Any]],
        meta: Dict[str, Any],
        names: List[Dict[str, Any]],
        past_values: List[Dict[str, Any]],
        power: int,
        pp: int,
        priority: int,
        stat_changes: List[Dict[str, Any]],
        super_contest_effect: Dict[str, Any],
        target: Dict[str, Any],
        type: Dict[str, Any],
    ) -> None:
        super().__init__(id=id, name=name)
        self.accuracy = accuracy
        self.contest_combos = ContestComboSets(**contest_combos)
        self.contest_effect = Url(**contest_effect)
        self.contest_type = MinimalResource(**contest_type)
        self.damage_class = MinimalResource(**damage_class)
        self.effect_chance = effect_chance
        self.effect_entries = [
            VerboseEffect(**effect_entry) for effect_entry in effect_entries
        ]
        self.effect_changes = [
            AbilityEffectChange(**effect_change) for effect_change in effect_changes
        ]
        self.flavor_text_entries = [
            MoveFlavorText(**flavor_text_entry)
            for flavor_text_entry in flavor_text_entries
        ]
        self.generation = MinimalResource(**generation)
        self.learned_by_pokemon = [
            MinimalResource(**pokemon) for pokemon in learned_by_pokemon
        ]
        self.machines = [MachineVersionDetail(**machine) for machine in machines]
        self.meta = MoveMetaData(**meta)
        self.names = [Name(**name) for name in names]
        self.past_values = [
            PastMoveStatValues(**past_value) for past_value in past_values
        ]
        self.power = power
        self.pp = pp
        self.priority = priority
        self.stat_changes = [
            MoveStatChange(**stat_change) for stat_change in stat_changes
        ]
        self.super_contest_effect = Url(**super_contest_effect)
        self.target = MinimalResource(**target)
        self.type = MinimalResource(**type)


class ContestComboSets(Resource):
    normal: Optional["ContestComboDetail"]
    super: Optional["ContestComboDetail"]

    def __init__(
        self,
        *,
        normal: Optional[Dict[str, Any]],
        super: Optional[Dict[str, Any]],
    ) -> None:
        self.normal = ContestComboDetail(**normal) if normal is not None else None
        self.super = ContestComboDetail(**super) if super is not None else None


class ContestComboDetail(Resource):
    use_before: Optional[List[MinimalResource["Move"]]]
    use_after: Optional[List[MinimalResource["Move"]]]

    def __init__(
        self,
        *,
        use_before: Optional[List[Dict[str, Any]]],
        use_after: Optional[List[Dict[str, Any]]],
    ) -> None:
        self.use_before = (
            [MinimalResource(**move) for move in use_before]
            if use_before is not None
            else None
        )
        self.use_after = (
            [MinimalResource(**move) for move in use_after]
            if use_after is not None
            else None
        )


class MoveFlavorText(Resource):
    flavor_text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self,
        *,
        flavor_text: str,
        language: Dict[str, Any],
        version_group: Dict[str, Any],
    ) -> None:
        self.flavor_text = flavor_text
        self.language = MinimalResource(**language)
        self.version_group = MinimalResource(**version_group)


class MoveMetaData(Resource):
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

    def __init__(
        self,
        *,
        ailment: Dict[str, Any],
        category: Dict[str, Any],
        min_hits: int,
        max_hits: int,
        min_turns: int,
        max_turns: int,
        drain: int,
        healing: int,
        crit_rate: int,
        ailment_chance: int,
        flinch_chance: int,
        stat_chance: int,
    ) -> None:
        self.ailment = MinimalResource(**ailment)
        self.category = MinimalResource(**category)
        self.min_hits = min_hits
        self.max_hits = max_hits
        self.min_turns = min_turns
        self.max_turns = max_turns
        self.drain = drain
        self.healing = healing
        self.crit_rate = crit_rate
        self.ailment_chance = ailment_chance
        self.flinch_chance = flinch_chance
        self.stat_chance = stat_chance


class MoveStatChange(Resource):
    change: int
    stat: MinimalResource["Stat"]

    def __init__(
        self,
        *,
        change: int,
        stat: Dict[str, Any],
    ) -> None:
        self.change = change
        self.stat = MinimalResource(**stat)


class PastMoveStatValues(Resource):
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: List["VerboseEffect"]
    type: MinimalResource["NaturalGiftType"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self,
        *,
        accuracy: int,
        effect_chance: int,
        power: int,
        pp: int,
        effect_entries: List[Dict[str, Any]],
        type: Dict[str, Any],
        version_group: Dict[str, Any],
    ) -> None:
        self.accuracy = accuracy
        self.effect_chance = effect_chance
        self.power = power
        self.pp = pp
        self.effect_entries = [
            VerboseEffect(**effect_entry) for effect_entry in effect_entries
        ]
        self.type = MinimalResource(**type)
        self.version_group = MinimalResource(**version_group)
