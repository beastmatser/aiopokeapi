from typing import TYPE_CHECKING, List, Optional

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

    def __init__(self, data) -> None:
        super().__init__(data)
        self.affecting_moves = MoveStatAffectSets(data["affecting_moves"])
        self.affecting_natures = NatureStatAffectSets(data["affecting_natures"])
        self.characteristics = [
            Url(characteristic_data["url"])
            for characteristic_data in data["characteristics"]
        ]
        self.game_index = data["game_index"]
        self.is_battle_only = data["is_battle_only"]
        self.move_damage_class = (
            MinimalResource(data["move_damage_class"])
            if data["move_damage_class"] is not None
            else None
        )
        self.names = [Name(name_data) for name_data in data["names"]]


class MoveStatAffectSets(Resource):
    increase: List["MoveStatAffect"]
    decrease: List["MoveStatAffect"]

    def __init__(self, data) -> None:
        self.increase = [
            MoveStatAffect(increase_data) for increase_data in data["increase"]
        ]
        self.decrease = [
            MoveStatAffect(decrease_data) for decrease_data in data["decrease"]
        ]


class MoveStatAffect(Resource):
    change: int
    move: MinimalResource["Move"]

    def __init__(self, data) -> None:
        self.change = data["change"]
        self.move = MinimalResource(data["move"])


class NatureStatAffectSets(Resource):
    increase: List[MinimalResource["Nature"]]
    decrease: List[MinimalResource["Nature"]]

    def __init__(self, data) -> None:
        self.increase = [
            MinimalResource(increase_data) for increase_data in data["increase"]
        ]
        self.decrease = [
            MinimalResource(decrease_data) for decrease_data in data["decrease"]
        ]
