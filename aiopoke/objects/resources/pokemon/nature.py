from typing import TYPE_CHECKING, Any, Dict, List, Optional

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import BerryFlavor, MoveBatteStyle
    from aiopoke.objects.resources.pokemon import PokeathlonStat


class Nature(NamedResource):
    decreased_stat: Optional[MinimalResource["PokeathlonStat"]]
    hates_flavor: Optional[MinimalResource["BerryFlavor"]]
    increased_stat: Optional[MinimalResource["PokeathlonStat"]]
    likes_flavor: Optional[MinimalResource["BerryFlavor"]]
    move_battle_style_preferences: List["MoveBattleStylePreference"]
    names: List["Name"]
    pokeathlon_stat_changes: List["NatureStatChange"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        decreased_stat: Optional[Dict[str, Any]],
        hates_flavor: Optional[Dict[str, Any]],
        increased_stat: Optional[Dict[str, Any]],
        likes_flavor: Optional[Dict[str, Any]],
        move_battle_style_preferences: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        pokeathlon_stat_changes: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.decreased_stat = (
            MinimalResource(**decreased_stat) if decreased_stat is not None else None
        )
        self.hates_flavor = (
            MinimalResource(**hates_flavor) if hates_flavor is not None else None
        )
        self.increased_stat = (
            MinimalResource(**increased_stat) if increased_stat is not None else None
        )
        self.likes_flavor = (
            MinimalResource(**likes_flavor) if likes_flavor is not None else None
        )
        self.move_battle_style_preferences = [
            MoveBattleStylePreference(**move_battle_style_preference)
            for move_battle_style_preference in move_battle_style_preferences
        ]
        self.names = [Name(**name) for name in names]
        self.pokeathlon_stat_changes = [
            NatureStatChange(**pokeathlon_stat_change)
            for pokeathlon_stat_change in pokeathlon_stat_changes
        ]


class NatureStatChange(Resource):
    max_change: int
    pokeathlon_stat: MinimalResource["PokeathlonStat"]

    def __init__(
        self,
        *,
        max_change: int,
        pokeathlon_stat: Dict[str, Any],
    ) -> None:
        self.max_change = max_change
        self.pokeathlon_stat = MinimalResource(**pokeathlon_stat)


class MoveBattleStylePreference(Resource):
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: MinimalResource["MoveBatteStyle"]

    def __init__(
        self,
        *,
        low_hp_preference: int,
        high_hp_preference: int,
        move_battle_style: Dict[str, Any],
    ) -> None:
        self.low_hp_preference = low_hp_preference
        self.high_hp_preference = high_hp_preference
        self.move_battle_style = MinimalResource(**move_battle_style)
