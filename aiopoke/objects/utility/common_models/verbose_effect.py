from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class VerboseEffect(Resource):
    effect: str
    short_effect: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.effect = data["effect"]
        self.short_effect = data["short_effect"]
        self.language = MinimalResource(data["language"])
