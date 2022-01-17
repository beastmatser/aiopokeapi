from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from ...utility import Name
from ...utility import NamedResource

if TYPE_CHECKING:
    from ...resources import VersionGroup


class Version(NamedResource):
    version_group: MinimalResource["VersionGroup"]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.version_group = MinimalResource(data["version_group"])

    def __repr__(self) -> str:
        return f"<Version id_={self.id} name='{self.name}' names={self.names} version_group={self.version_group}>"
