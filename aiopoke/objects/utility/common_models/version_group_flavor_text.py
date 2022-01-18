from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import VersionGroup
    from aiopoke.objects.utility import Language


class VersionGroupFlavorText(Resource):
    text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.text = data["text"]
        self.language = MinimalResource(data["language"])
        self.version_group = MinimalResource(data["version_group"])
