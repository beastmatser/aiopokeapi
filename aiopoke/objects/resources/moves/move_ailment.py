from typing import TYPE_CHECKING, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class MoveAilment(NamedResource):
    moves: List[MinimalResource["Move"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.moves = [MinimalResource(item_data) for item_data in data["moves"]]
        self.names = [Name(name_data) for name_data in data["names"]]
