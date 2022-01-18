from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Version


class VersionGameIndex(Resource):
    game_index: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.game_index = data["game_index"]
        self.version = MinimalResource(data["version"])
