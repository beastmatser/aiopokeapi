from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import Berry


class BerryFirmness(NamedResource):
    berries: List[MinimalResource["Berry"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        berries: List[Dict[str, Any]],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.berries = [MinimalResource(**berry) for berry in berries]
        self.names = [Name(**name) for name in names]
