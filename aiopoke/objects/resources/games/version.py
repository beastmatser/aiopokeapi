from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import VersionGroup


class Version(NamedResource):
    version_group: MinimalResource["VersionGroup"]
    names: List["Name"]

    def __init__(
        self, version_group: Dict[str, Any], names: List[Dict[str, Any]]
    ) -> None:
        self.version_group = MinimalResource(**version_group)
        self.names = [Name(**name) for name in names]
