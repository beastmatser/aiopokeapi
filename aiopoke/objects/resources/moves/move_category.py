from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Description
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class MoveCategory(NamedResource):
    description: str
    descriptions: Tuple["Description", ...]
    moves: Tuple[MinimalResource["Move"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = [
            name_data["description"]
            for name_data in data["descriptions"]
            if name_data["language"]["name"] == "en"
        ][0]
        self.descriptions = tuple(
            Description(description_data) for description_data in data["descriptions"]
        )
        self.moves = tuple(MinimalResource(move_data) for move_data in data["moves"])
