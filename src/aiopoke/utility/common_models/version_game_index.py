from ...minimal_resources import MinimalVersion


class VersionGameIndex:
    game_index: int
    version: "MinimalVersion"

    def __init__(self, data) -> None:
        self.game_index = data["game_index"]
        self.version = MinimalVersion(data["version"])

    def __repr__(self) -> str:
        return f"<VersionGameIndex game_index={self.game_index} version={self.version}>"
