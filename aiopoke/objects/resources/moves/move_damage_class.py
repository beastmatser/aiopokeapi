from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility.common_models import Description, Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class MoveDamageClass(NamedResource):
    descriptions: List["Description"]
    moves: List[MinimalResource["Move"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        descriptions: List[Dict[str, Any]],
        moves: List[Dict[str, Any]],
        names: List[Dict[str, Any]]
    ) -> None:
        self.descriptions = [Description(**description) for description in descriptions]
        self.moves = [MinimalResource(**move) for move in moves]
        self.names = [Name(**name) for name in names]
