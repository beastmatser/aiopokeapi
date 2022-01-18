from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import BerryFlavor


class ContestType(NamedResource):
    berry_flavor: MinimalResource["BerryFlavor"]
    names: List["ContestName"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        berry_flavor: Dict[str, Any],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.berry_flavor = MinimalResource(**berry_flavor)
        self.names = [ContestName(**name) for name in names]


class ContestName(Name):
    color: str

    def __init__(self, *, color: str, name: str) -> None:
        super().__init__(name=name)
        self.color = color
