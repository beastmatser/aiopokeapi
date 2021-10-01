from typing import List, TYPE_CHECKING
from ...utility import FlavorText
from ...minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...resources.moves import Move


class SuperContestEffect:
    appeal: int
    flavor_text_entry: "FlavorText"
    flavor_text_entries: List["FlavorText"]
    id_: int
    moves: List[MinimalResource["Move"]]

    def __init__(self, data) -> None:
        self.appeal = data["appeal"]
        self.flavor_text_entry = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        ][0]
        self.flavor_text_entries = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.id_ = data["id"]
        self.moves = [MinimalResource(move_data) for move_data in data["moves"]]

    def __repr__(self) -> str:
        return (
            f"<SuperContestEffect appeal={self.appeal} flavor_text_entry={self.flavor_text_entry} "
            f"flavor_text_entries={self.flavor_text_entries} id_={self.id_} moves={self.moves}>"
        )
