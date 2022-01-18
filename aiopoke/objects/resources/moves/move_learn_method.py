from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Description
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import VersionGroup


class MoveLearnMethod(NamedResource):
    descriptions: List["Description"]
    names: List["Name"]
    version_groups: List[MinimalResource["VersionGroup"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.descriptions = [
            Description(description_data) for description_data in data["descriptions"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.version_groups = [
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        ]
