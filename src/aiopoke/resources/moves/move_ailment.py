from typing import List
from ...minimal_resources import MinimalMove
from ...utility.common_models import Name, NamedResource


class MoveAilment(NamedResource):
    moves: List["MinimalMove"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.moves = [MinimalMove(item_data) for item_data in data["moves"]]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<MoveAilment id_={self.id_} moves={self.moves} name={self.name} names={self.names}>"
