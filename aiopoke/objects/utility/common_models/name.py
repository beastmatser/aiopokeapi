from typing import TYPE_CHECKING

from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class Name(Resource):
    name: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.name = data["name"]
        self.language = MinimalResource(data["language"])
