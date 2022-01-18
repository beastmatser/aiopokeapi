from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import Berry
    from aiopoke.objects.resources.contests.contest_type import ContestType


class BerryFlavor(NamedResource):
    berries: List["FlavorBerryMap"]
    contest_type: MinimalResource["ContestType"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        berries: List[Dict[str, Any]],
        contest_type: Dict[str, Any],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.berries = [FlavorBerryMap(**berry) for berry in berries]
        self.contest_type = MinimalResource(**contest_type)
        self.names = [Name(**name) for name in names]


class FlavorBerryMap(Resource):
    potency: int
    berry: MinimalResource["Berry"]

    def __init__(self, *, potency: int, berry: Dict[str, Any]) -> None:
        self.potency = potency
        self.berry = MinimalResource(**berry)
