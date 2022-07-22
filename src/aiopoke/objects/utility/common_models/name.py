from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class Name(Resource):
    name: str
    language: MinimalResource["Language"]

    def __init__(
        self,
        *,
        name: str,
        language: Dict[str, Any],
    ):
        self.name = name
        self.language = MinimalResource(**language)
