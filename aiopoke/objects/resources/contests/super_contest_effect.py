from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility import FlavorText
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.moves import Move


class SuperContestEffect(Resource):
    appeal: int
    flavor_text_entry: "FlavorText"
    flavor_text_entries: Tuple["FlavorText", ...]
    id_: int
    moves: Tuple[MinimalResource["Move"], ...]

    def __init__(self, data) -> None:
        self.appeal = data["appeal"]
        self.flavor_text_entry = tuple(
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        )[0]
        self.flavor_text_entries = tuple(
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        )
        self.id_ = data["id"]
        self.moves = tuple(MinimalResource(move_data) for move_data in data["moves"])
