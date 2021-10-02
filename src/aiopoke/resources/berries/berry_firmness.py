from typing import TYPE_CHECKING, Tuple

from ...minimal_resources import MinimalResource
from ...utility import Name, NamedResource

if TYPE_CHECKING:
    from . import Berry


class BerryFirmness(NamedResource):
    berries: Tuple[MinimalResource["Berry"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berries = tuple(
            MinimalResource(berry_data) for berry_data in data["berries"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])

    def __repr__(self) -> str:
        return f"<BerryFirmness berries={self.berries} id_={self.id_} name='{self.name}' names={self.names}>"
