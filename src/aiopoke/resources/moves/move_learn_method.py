from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource, Description

if TYPE_CHECKING:
    from ...resources import VersionGroup


class MoveLearnMethod(NamedResource):
    description: str
    descriptions: List["Description"]
    names: List["Name"]
    version_groups: List[MinimalResource["VersionGroup"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = [
            description_data["description"]
            for description_data in data["descriptions"]
            if description_data["language"]["name"] == "en"
        ][0]
        self.descriptions = [
            Description(description_data) for description_data in data["descriptions"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.version_groups = [
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        ]

    def __repr__(self) -> str:
        return (
            f"<MoveLearnMethod description='{self.description}' descriptions={self.descriptions} id_={self.id_} "
            f"name='{self.name}' version_groups={self.version_groups}>"
        )
