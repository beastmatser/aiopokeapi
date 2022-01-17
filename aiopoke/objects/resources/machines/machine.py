from typing import TYPE_CHECKING

from ....minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...resources import Item, Move, VersionGroup


class Machine:
    id: int
    item: MinimalResource["Item"]
    move: MinimalResource["Move"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.item = MinimalResource(data["item"])
        self.move = MinimalResource(data["move"])
        self.version_group = MinimalResource(data["version_group"])

    def __repr__(self) -> str:
        return f"<Machine id_={self.id} item={self.item} move={self.move} version_group={self.version_group}>"
