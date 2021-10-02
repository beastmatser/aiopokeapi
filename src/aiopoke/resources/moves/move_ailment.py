from typing import TYPE_CHECKING, Tuple

from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from . import Move


class MoveAilment(NamedResource):
    moves: Tuple[MinimalResource["Move"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.moves = tuple(MinimalResource(item_data) for item_data in data["moves"])
        self.names = tuple(Name(name_data) for name_data in data["names"])

    def __repr__(self) -> str:
        return f"<MoveAilment id_={self.id_} moves={self.moves} name={self.name} names={self.names}>"
