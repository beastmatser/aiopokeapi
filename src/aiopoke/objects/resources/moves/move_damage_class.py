from typing import Any
from typing import Dict
from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Description
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource
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
        id: int,
        name: str,
        descriptions: List[Dict[str, Any]],
        moves: List[Dict[str, Any]],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.descriptions = [Description(**description) for description in descriptions]
        self.moves = [MinimalResource(**move) for move in moves]
        self.names = [Name(**name) for name in names]
