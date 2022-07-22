from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class Effect(Resource):
    effect: str
    language: MinimalResource["Language"]

    def __init__(
        self,
        *,
        effect: str,
        language: Dict[str, Any],
    ):
        self.effect = effect
        self.language = MinimalResource(**language)
