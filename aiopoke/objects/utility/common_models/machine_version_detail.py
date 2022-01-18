from typing import TYPE_CHECKING

from aiopoke.utils.minimal_resources import MinimalResource, Url
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Machine, VersionGroup


class MachineVersionDetail(Resource):
    machine: Url["Machine"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.machine = Url(data["machine"])
        self.version_group = MinimalResource(data["version_group"])
