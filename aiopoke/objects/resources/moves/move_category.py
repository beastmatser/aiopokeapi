from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Description
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class MoveCategory(NamedResource):
    descriptions: List["Description"]
    moves: List[MinimalResource["Move"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.descriptions = [
            Description(description_data) for description_data in data["descriptions"]
        ]
        self.moves = [MinimalResource(move_data) for move_data in data["moves"]]
