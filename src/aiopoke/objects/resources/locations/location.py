from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from aiopoke.objects.utility import GenerationGameIndex
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.locations import LocationArea, Region


class Location(NamedResource):
    areas: List[MinimalResource["LocationArea"]]
    game_indices: List["GenerationGameIndex"]
    region: Optional[MinimalResource["Region"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        areas: List[Dict[str, Any]],
        game_indices: List[Dict[str, Any]],
        region: Optional[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.areas = [MinimalResource(**area) for area in areas]
        self.game_indices = [
            GenerationGameIndex(**game_index) for game_index in game_indices
        ]
        self.region = MinimalResource(**region) if region is not None else None
        self.names = [Name(**name) for name in names]
