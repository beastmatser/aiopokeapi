from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Description, Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import VersionGroup


class MoveLearnMethod(NamedResource):
    descriptions: List["Description"]
    names: List["Name"]
    version_groups: List[MinimalResource["VersionGroup"]]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        descriptions: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        version_groups: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.descriptions = [Description(**description) for description in descriptions]
        self.names = [Name(**name) for name in names]
        self.version_groups = [
            MinimalResource(**version_group) for version_group in version_groups
        ]
