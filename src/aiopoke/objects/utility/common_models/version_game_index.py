from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Version


class VersionGameIndex(Resource):
    game_index: int
    version: MinimalResource["Version"]

    def __init__(self, *, game_index: int, version: Dict[str, Any]):
        self.game_index = game_index
        self.version = MinimalResource(**version)
