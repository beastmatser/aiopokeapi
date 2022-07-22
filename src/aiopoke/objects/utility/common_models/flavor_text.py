from typing import TYPE_CHECKING, Any, Dict, Optional

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Version
    from aiopoke.objects.utility import Language


class FlavorText(Resource):
    flavor_text: str
    language: MinimalResource["Language"]
    version: Optional[MinimalResource["Version"]]

    def __init__(
        self,
        *,
        flavor_text: str,
        language: Dict[str, Any],
        version: Optional[Dict[str, Any]] = None,
    ):
        self.flavor_text = flavor_text
        self.language = MinimalResource(**language)
        self.version = MinimalResource(**version) if version is not None else None
