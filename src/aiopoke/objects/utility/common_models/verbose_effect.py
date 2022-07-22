from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class VerboseEffect(Resource):
    effect: str
    short_effect: str
    language: MinimalResource["Language"]

    def __init__(self, *, effect: str, short_effect: str, language: Dict[str, Any]):
        self.effect = effect
        self.short_effect = short_effect
        self.language = MinimalResource(**language)
