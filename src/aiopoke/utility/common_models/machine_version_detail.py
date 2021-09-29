from ...minimal_resources import MinimalVersionGroup, MachineUrl


class MachineVersionDetail:
    machine: MachineUrl
    version_group: "MinimalVersionGroup"

    def __init__(self, data) -> None:
        self.machine = MachineUrl(data["machine"])
        self.version_group = MinimalVersionGroup(data["version_group"])

    def __repr__(self) -> str:
        return f"<MachineVersionDetail machine={self.machine} version_group={self.version_group}>"
