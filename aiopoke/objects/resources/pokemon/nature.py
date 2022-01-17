from typing import Optional
from typing import Tuple
from typing import TYPE_CHECKING

from ....minimal_resources import MinimalResource
from ...utility.common_models import Name
from ...utility.common_models import NamedResource

if TYPE_CHECKING:
    from . import PokeathlonStat
    from ...resources import MoveBatteStyle, BerryFlavor


class Nature(NamedResource):
    decreased_stat: Optional[MinimalResource["PokeathlonStat"]]
    hates_flavor: Optional[MinimalResource["BerryFlavor"]]
    increased_stat: Optional[MinimalResource["PokeathlonStat"]]
    likes_flavor: Optional[MinimalResource["BerryFlavor"]]
    move_battle_style_preferences: Tuple["MoveBattleStylePreference", ...]
    names: Tuple["Name", ...]
    pokeathlon_stat_changes: Tuple["NatureStatChange", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.decreased_stat = (
            MinimalResource(data["decreased_stat"])
            if data["decreased_stat"] is not None
            else None
        )
        self.hates_flavor = (
            MinimalResource(data["hates_flavor"])
            if data["hates_flavor"] is not None
            else None
        )
        self.increased_stat = (
            MinimalResource(data["increased_stat"])
            if data["increased_stat"] is not None
            else None
        )
        self.likes_flavor = (
            MinimalResource(data["likes_flavor"])
            if data["likes_flavor"] is not None
            else None
        )
        self.move_battle_style_preferences = tuple(
            MoveBattleStylePreference(move_battle_style_preference_data)
            for move_battle_style_preference_data in data[
                "move_battle_style_preferences"
            ]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.pokeathlon_stat_changes = tuple(
            NatureStatChange(pokeathlon_stat_change_data)
            for pokeathlon_stat_change_data in data["pokeathlon_stat_changes"]
        )

    def __repr__(self) -> str:
        return (
            f"<Nature decreased_stat={self.decreased_stat} hates_flavor={self.hates_flavor} increased_stat={self.increased_stat} id_={self.id} "
            f"likes_flavor={self.likes_flavor} move_battle_style_preferences={self.move_battle_style_preferences} "
            f"name='{self.name}' names={self.names} pokeathlon_stat_changes={self.pokeathlon_stat_changes}>"
        )


class NatureStatChange:
    max_change: int
    pokeathlon_stat: MinimalResource["PokeathlonStat"]

    def __init__(self, data) -> None:
        self.max_change = data["max_change"]
        self.pokeathlon_stat = MinimalResource(data["pokeathlon_stat"])

    def __repr__(self) -> str:
        return f"<NatureStatChange max_change={self.max_change} pokeathlon_stat={self.pokeathlon_stat}>"


class MoveBattleStylePreference:
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: MinimalResource["MoveBatteStyle"]

    def __init__(self, data) -> None:
        self.low_hp_preference = data["low_hp_preference"]
        self.high_hp_preference = data["high_hp_preference"]
        self.move_battle_style = MinimalResource(data["move_battle_style"])

    def __repr__(self) -> str:
        return (
            f"<MoveBattleStylePreference low_hp_preference={self.low_hp_preference} high_hp_preference={self.high_hp_preference} "
            f"move_battle_style={self.move_battle_style}>"
        )
