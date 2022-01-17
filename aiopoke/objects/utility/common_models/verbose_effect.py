from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...utility import Language


class VerboseEffect:
    effect: str
    short_effect: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.effect = data["effect"]
        self.short_effect = data["short_effect"]
        self.language = MinimalResource(data["language"])

    def __repr__(self) -> str:
        return f"<VerboseEffect effect='{self.effect}' short_effect='{self.short_effect}' language={self.language}>"
