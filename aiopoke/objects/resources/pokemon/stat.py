from typing import Optional
from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.minimal_resources import Url
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import Characteristic, Nature
    from aiopoke.objects.resources import Move, MoveDamageClass


class Stat(NamedResource):
    affecting_moves: "MoveStatAffectSets"
    affecting_natures: "NatureStatAffectSets"
    characteristics: Tuple[Url["Characteristic"], ...]
    game_index: int
    is_battle_only: bool
    move_damage_class: Optional[MinimalResource["MoveDamageClass"]]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.affecting_moves = MoveStatAffectSets(data["affecting_moves"])
        self.affecting_natures = NatureStatAffectSets(data["affecting_natures"])
        self.characteristics = tuple(
            Url(characteristic_data["url"])
            for characteristic_data in data["characteristics"]
        )
        self.game_index = data["game_index"]
        self.is_battle_only = data["is_battle_only"]
        self.move_damage_class = (
            MinimalResource(data["move_damage_class"])
            if data["move_damage_class"] is not None
            else None
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])


class MoveStatAffectSets(Resource):
    increase: Tuple["MoveStatAffect", ...]
    decrease: Tuple["MoveStatAffect", ...]

    def __init__(self, data) -> None:
        self.increase = tuple(
            MoveStatAffect(increase_data) for increase_data in data["increase"]
        )
        self.decrease = tuple(
            MoveStatAffect(decrease_data) for decrease_data in data["decrease"]
        )


class MoveStatAffect(Resource):
    change: int
    move: MinimalResource["Move"]

    def __init__(self, data) -> None:
        self.change = data["change"]
        self.move = MinimalResource(data["move"])


class NatureStatAffectSets(Resource):
    increase: Tuple[MinimalResource["Nature"], ...]
    decrease: Tuple[MinimalResource["Nature"], ...]

    def __init__(self, data) -> None:
        self.increase = tuple(
            MinimalResource(increase_data) for increase_data in data["increase"]
        )
        self.decrease = tuple(
            MinimalResource(decrease_data) for decrease_data in data["decrease"]
        )
