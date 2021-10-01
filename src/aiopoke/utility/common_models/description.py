from typing import TYPE_CHECKING
from ...minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...utility import Language


class Description:
    description: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.description = data["description"]
        self.language = MinimalResource(data["language"])

    def __repr__(self) -> str:
        return f"<Description description='{self.description}' language={self.language}>"
