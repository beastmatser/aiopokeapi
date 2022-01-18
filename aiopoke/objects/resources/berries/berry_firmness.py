from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource

from aiopoke.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import Berry


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
        return f"<BerryFirmness berries={self.berries} id_={self.id} name='{self.name}' names={self.names}>"
