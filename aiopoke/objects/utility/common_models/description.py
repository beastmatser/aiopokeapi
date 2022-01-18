from typing import TYPE_CHECKING

from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class Description(Resource):
    description: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.description = data["description"]
        self.language = MinimalResource(data["language"])
