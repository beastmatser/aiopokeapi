from typing import TYPE_CHECKING

from ....minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...resources import VersionGroup
    from ...utility import Language


class VersionGroupFlavorText:
    text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.text = data["text"]
        self.language = MinimalResource(data["language"])
        self.version_group = MinimalResource(data["version_group"])

    def __repr__(self) -> str:
        return f"<VersionGroupFlavorText text='{self.text}' language={self.language} version_group={self.version_group}>"
