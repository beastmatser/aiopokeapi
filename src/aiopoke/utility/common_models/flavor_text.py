from typing import TYPE_CHECKING, Optional

from ...minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...resources import Version
    from ...utility import Language


class FlavorText:
    flavor_text: str
    language: MinimalResource["Language"]
    version: Optional[MinimalResource["Version"]]

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalResource(data["language"])
        self.version = (
            MinimalResource(data["version"])
            if data.get("version") is not None
            else None
        )

    def __repr__(self) -> str:
        return f"<FlavorText flavor_text='{self.flavor_text}' language={self.language} version={self.version}>"
