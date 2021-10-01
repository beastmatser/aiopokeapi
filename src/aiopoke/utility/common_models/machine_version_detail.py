from typing import TYPE_CHECKING
from ...minimal_resources import MinimalResource, Url

if TYPE_CHECKING:
    from ...resources import Machine, VersionGroup


class MachineVersionDetail:
    machine: Url["Machine"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.machine = Url(data["machine"])
        self.version_group = MinimalResource(data["version_group"])

    def __repr__(self) -> str:
        return f"<MachineVersionDetail machine={self.machine} version_group={self.version_group}>"
