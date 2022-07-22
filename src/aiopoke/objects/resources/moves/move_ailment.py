from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class MoveAilment(NamedResource):
    moves: List[MinimalResource["Move"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        moves: List[Dict[str, Any]],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.moves = [MinimalResource(**move) for move in moves]
        self.names = [Name(**name) for name in names]
