from ...minimal_resources import MinimalItem, MinimalVersionGroup, MinimalMove


class Machine:
    id_: int
    item: MinimalItem
    move: MinimalMove
    version_group: MinimalVersionGroup

    def __init__(self, data) -> None:
        self.id_ = data["id"]
        self.item = MinimalItem(data["item"])
        self.move = MinimalMove(data["move"])
        self.version_group = MinimalVersionGroup(data["version_group"])

    def __repr__(self) -> str:
        return f"<Machine id_={self.id_} item={self.item} move={self.move} version_group={self.version_group}>"
