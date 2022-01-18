from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import VersionGroup


class Version(NamedResource):
    version_group: MinimalResource["VersionGroup"]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.version_group = MinimalResource(data["version_group"])
