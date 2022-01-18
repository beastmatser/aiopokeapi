from typing import TYPE_CHECKING

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class Effect(Resource):
    effect: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.effect = data["effect"]
        self.language = MinimalResource(data["language"])
