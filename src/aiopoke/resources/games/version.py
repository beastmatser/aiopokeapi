from typing import List
from ...minimal_resources import MinimalVersionGroup
from ...utility import Name, NamedResource


class Version(NamedResource):
    version_group: "MinimalVersionGroup"
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.names = [Name(name_data) for name_data in data["names"]]
        self.version_group = MinimalVersionGroup(data["version_group"])

    def __repr__(self) -> str:
        return f"<Version id_={self.id_} name='{self.name}' names={self.names} version_group={self.version_group}>"
