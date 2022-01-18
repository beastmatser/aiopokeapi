from typing import TYPE_CHECKING, List

from aiopoke.objects.utility import FlavorText
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class SuperContestEffect(Resource):
    appeal: int
    flavor_text_entries: List["FlavorText"]
    id_: int
    moves: List[MinimalResource["Move"]]

    def __init__(self, data) -> None:
        self.appeal = data["appeal"]
        self.flavor_text_entries = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.id_ = data["id"]
        self.moves = [MinimalResource(move_data) for move_data in data["moves"]]
