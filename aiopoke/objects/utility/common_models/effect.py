from typing import TYPE_CHECKING

from ....minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...utility import Language


class Effect:
    effect: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.effect = data["effect"]
        self.language = MinimalResource(data["language"])

    def __repr__(self) -> str:
        return f"<Effect effect='{self.effect}' language={self.language}>"
