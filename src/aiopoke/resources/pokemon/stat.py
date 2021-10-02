from typing import Tuple, Optional, TYPE_CHECKING
from ...minimal_resources import MinimalResource, Url
from ...utility import Name, NamedResource

if TYPE_CHECKING:
    from . import Characteristic, Nature
    from ...resources import Move, MoveDamageClass


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
        self.characteristics = tuple(Url(characteristic_data["url"]) for characteristic_data in data["characteristics"])
        self.game_index = data["game_index"]
        self.is_battle_only = data["is_battle_only"]
        self.move_damage_class = MinimalResource(data["move_damage_class"]) if data["move_damage_class"] is not None else None
        self.names = tuple(Name(name_data) for name_data in data["names"])

    def __repr__(self) -> str:
        return (
            f"<Stat affecting_moves={self.affecting_moves} affecting_natures={self.affecting_natures} characteristics={self.characteristics} "
            f"game_index={self.game_index} id_={self.id_} is_battle_only={self.is_battle_only} move_damage_class={self.move_damage_class} "
            f"name='{self.name}' names={self.names}>"
        )


class MoveStatAffectSets:
    increase: Tuple["MoveStatAffect", ...]
    decrease: Tuple["MoveStatAffect", ...]

    def __init__(self, data) -> None:
        self.increase = tuple(MoveStatAffect(increase_data) for increase_data in data["increase"])
        self.decrease = tuple(MoveStatAffect(decrease_data) for decrease_data in data["decrease"])

    def __repr__(self) -> str:
        return f"<MoveStatAffectSets increase={self.increase} decrease={self.decrease}>"


class MoveStatAffect:
    change: int
    move: MinimalResource["Move"]

    def __init__(self, data) -> None:
        self.change = data["change"]
        self.move = MinimalResource(data["move"])

    def __repr__(self) -> str:
        return f"<MoveStatAffect change={self.change} move={self.move}>"


class NatureStatAffectSets:
    increase: Tuple[MinimalResource["Nature"], ...]
    decrease: Tuple[MinimalResource["Nature"], ...]

    def __init__(self, data) -> None:
        self.increase = tuple(MinimalResource(increase_data) for increase_data in data["increase"])
        self.decrease = tuple(MinimalResource(decrease_data) for decrease_data in data["decrease"])

    def __repr__(self) -> str:
        return f"<NatureStatAffectSets increase={self.increase} decrease={self.decrease}>"
