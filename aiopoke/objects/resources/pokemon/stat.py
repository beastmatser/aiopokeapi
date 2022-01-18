from typing import TYPE_CHECKING, Any, Dict, List, Optional

from aiopoke.objects.utility import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource, Url
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Move, MoveDamageClass
    from aiopoke.objects.resources.pokemon import Characteristic, Nature


class Stat(NamedResource):
    affecting_moves: "MoveStatAffectSets"
    affecting_natures: "NatureStatAffectSets"
    characteristics: List[Url["Characteristic"]]
    game_index: int
    is_battle_only: bool
    move_damage_class: Optional[MinimalResource["MoveDamageClass"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        affecting_moves: Dict[str, Any],
        affecting_natures: Dict[str, Any],
        characteristics: List[Dict[str, Any]],
        game_index: int,
        is_battle_only: bool,
        move_damage_class: Optional[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ):
        super().__init__(id=id, name=name)
        self.affecting_moves = MoveStatAffectSets(**affecting_moves)
        self.affecting_natures = NatureStatAffectSets(**affecting_natures)
        self.characteristics = [
            Url(**characteristic) for characteristic in characteristics
        ]
        self.game_index = game_index
        self.is_battle_only = is_battle_only
        self.move_damage_class = (
            MinimalResource(**move_damage_class)
            if move_damage_class is not None
            else None
        )
        self.names = [Name(**name) for name in names]


class MoveStatAffectSets(Resource):
    increase: List["MoveStatAffect"]
    decrease: List["MoveStatAffect"]

    def __init__(
        self,
        *,
        increase: List[Dict[str, Any]],
        decrease: List[Dict[str, Any]],
    ) -> None:
        self.increase = [
            MoveStatAffect(**move_stat_affect) for move_stat_affect in increase
        ]
        self.decrease = [
            MoveStatAffect(**move_stat_affect) for move_stat_affect in decrease
        ]


class MoveStatAffect(Resource):
    change: int
    move: MinimalResource["Move"]

    def __init__(
        self,
        *,
        change: int,
        move: Dict[str, Any],
    ) -> None:
        self.change = change
        self.move = MinimalResource(**move)


class NatureStatAffectSets(Resource):
    increase: List[MinimalResource["Nature"]]
    decrease: List[MinimalResource["Nature"]]

    def __init__(
        self, *, increase: List[Dict[str, Any]], decrease: List[Dict[str, Any]]
    ) -> None:
        self.increase = [MinimalResource(**nature_data) for nature_data in increase]
        self.decrease = [MinimalResource(**nature_data) for nature_data in decrease]
