from typing import TYPE_CHECKING

from ....minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...utility import Language


class Name:
    name: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.name = data["name"]
        self.language = MinimalResource(data["language"])

    def __repr__(self) -> str:
        return f"<Name name='{self.name}' language={self.language}>"
