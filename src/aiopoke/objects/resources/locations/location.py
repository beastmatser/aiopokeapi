from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import GenerationGameIndex, Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.locations import LocationArea, Region


class Location(NamedResource):
    areas: List[MinimalResource["LocationArea"]]
    game_indices: List["GenerationGameIndex"]
    region: MinimalResource["Region"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        areas: List[Dict[str, Any]],
        game_indices: List[Dict[str, Any]],
        region: Dict[str, Any],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.areas = [MinimalResource(**area) for area in areas]
        self.game_indices = [
            GenerationGameIndex(**game_index) for game_index in game_indices
        ]
        self.region = MinimalResource(**region)
        self.names = [Name(**name) for name in names]
