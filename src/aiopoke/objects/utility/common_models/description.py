from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class Description(Resource):
    description: str
    language: MinimalResource["Language"]

    def __init__(
        self,
        *,
        description: str,
        language: Dict[str, Any],
    ):
        self.description = description
        self.language = MinimalResource(**language)
