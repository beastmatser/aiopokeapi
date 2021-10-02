from typing import TYPE_CHECKING, Tuple

from ...minimal_resources import MinimalResource
from ...utility.common_models import Description, Name, NamedResource

if TYPE_CHECKING:
    from ...resources import VersionGroup


class MoveLearnMethod(NamedResource):
    description: str
    descriptions: Tuple["Description", ...]
    names: Tuple["Name", ...]
    version_groups: Tuple[MinimalResource["VersionGroup"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = tuple(
            description_data["description"]
            for description_data in data["descriptions"]
            if description_data["language"]["name"] == "en"
        )[0]
        self.descriptions = tuple(
            Description(description_data) for description_data in data["descriptions"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.version_groups = tuple(
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        )

    def __repr__(self) -> str:
        return (
            f"<MoveLearnMethod description='{self.description}' descriptions={self.descriptions} id_={self.id_} "
            f"name='{self.name}' version_groups={self.version_groups}>"
        )
