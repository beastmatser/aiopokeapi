from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Item, Move, VersionGroup


class Machine(Resource):
    id: int
    item: MinimalResource["Item"]
    move: MinimalResource["Move"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self,
        *,
        id: int,
        item: Dict[str, Any],
        move: Dict[str, Any],
        version_group: Dict[str, Any]
    ) -> None:
        self.id = id
        self.item = MinimalResource(**item)
        self.move = MinimalResource(**move)
        self.version_group = MinimalResource(**version_group)
