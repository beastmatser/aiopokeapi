from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import VersionGroup


class Version(NamedResource):
    version_group: MinimalResource["VersionGroup"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        version_group: Dict[str, Any],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.version_group = MinimalResource(**version_group)
        self.names = [Name(**name) for name in names]
