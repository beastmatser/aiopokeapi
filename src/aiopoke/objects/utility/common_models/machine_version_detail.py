from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource, Url
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Machine, VersionGroup


class MachineVersionDetail(Resource):
    machine: Url["Machine"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self,
        *,
        machine: Dict[str, Any],
        version_group: Dict[str, Any],
    ):
        self.machine = Url(**machine)
        self.version_group = MinimalResource(**version_group)
