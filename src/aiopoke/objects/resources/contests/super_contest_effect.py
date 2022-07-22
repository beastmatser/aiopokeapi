from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import FlavorText
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class SuperContestEffect(Resource):
    appeal: int
    flavor_text_entries: List["FlavorText"]
    id: int
    moves: List[MinimalResource["Move"]]

    def __init__(
        self,
        *,
        id: int,
        appeal: int,
        flavor_text_entries: List[Dict[str, Any]],
        moves: List[Dict[str, Any]]
    ) -> None:
        self.id = id
        self.appeal = appeal
        self.flavor_text_entries = [
            FlavorText(**flavor_text_entry) for flavor_text_entry in flavor_text_entries
        ]
        self.moves = [MinimalResource(**move) for move in moves]
