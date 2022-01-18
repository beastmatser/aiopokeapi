from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Item, Move, VersionGroup


class Machine(Resource):
    id: int
    item: MinimalResource["Item"]
    move: MinimalResource["Move"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.item = MinimalResource(data["item"])
        self.move = MinimalResource(data["move"])
        self.version_group = MinimalResource(data["version_group"])
