from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class MoveAilment(NamedResource):
    moves: List[MinimalResource["Move"]]
    names: List["Name"]

    def __init__(
        self, *, moves: List[Dict[str, Any]], names: List[Dict[str, Any]]
    ) -> None:
        self.moves = [MinimalResource(**move) for move in moves]
        self.names = [Name(**name) for name in names]
