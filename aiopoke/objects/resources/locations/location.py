from typing import List
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
    region: MinimalResource["Region"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.areas = [MinimalResource(area_data) for area_data in data["areas"]]
        self.game_indices = [
            GenerationGameIndex(game_indice_data)
            for game_indice_data in data["game_indices"]
        ]
        self.region = MinimalResource(data["region"])
        self.names = [Name(name_data) for name_data in data["names"]]
