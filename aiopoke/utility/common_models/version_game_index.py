from typing import TYPE_CHECKING

from ...minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...resources import Version


class VersionGameIndex:
    game_index: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.game_index = data["game_index"]
        self.version = MinimalResource(data["version"])

    def __repr__(self) -> str:
        return f"<VersionGameIndex game_index={self.game_index} version={self.version}>"
