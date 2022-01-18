from typing import TYPE_CHECKING, List, Dict, Any

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
        descriptions: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        version_groups: List[Dict[str, Any]],
    ) -> None:
        self.descriptions = [Description(**description) for description in descriptions]
        self.names = [Name(**name) for name in names]
        self.version_groups = [
            MinimalResource(**version_group) for version_group in version_groups
        ]
