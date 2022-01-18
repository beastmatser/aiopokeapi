from typing import TYPE_CHECKING, Optional

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Version
    from aiopoke.objects.utility import Language


class FlavorText(Resource):
    flavor_text: str
    language: MinimalResource["Language"]
    version: Optional[MinimalResource["Version"]]

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalResource(data["language"])
        self.version = (
            MinimalResource(data["version"])
            if data.get("version") is not None
            else None
        )
