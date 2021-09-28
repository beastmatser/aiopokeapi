from typing import List
from ...minimal_resources import MinimalMove
from ...utility.common_models import Name, NamedResource, Description


class MoveTarget(NamedResource):
    description: str
    descriptions: List["Description"]
    moves: List["MinimalMove"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = [
            name_data["name"]
            for name_data in data["names"]
            if name_data["language"]["name"] == "en"
        ][0]
        self.descriptions = [Description(description_data) for description_data in data["descriptions"]]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.moves = [MinimalMove(move_data) for move_data in data["moves"]]

    def __repr__(self) -> str:
        return f"<MoveTarget description='{self.description}' descriptions={self.descriptions} id_={self.id_} moves={self.moves} name='{self.name}'>"
