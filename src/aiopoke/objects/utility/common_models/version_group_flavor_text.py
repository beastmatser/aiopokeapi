from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import VersionGroup
    from aiopoke.objects.utility import Language


class VersionGroupFlavorText(Resource):
    text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self, *, text: str, language: Dict[str, Any], version_group: Dict[str, Any]
    ):
        self.text = text
        self.language = MinimalResource(**language)
        self.version_group = MinimalResource(**version_group)
