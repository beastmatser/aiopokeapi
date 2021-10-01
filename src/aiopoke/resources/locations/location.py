from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility import Name, NamedResource, GenerationGameIndex

if TYPE_CHECKING:
    from . import LocationArea, Region


class Location(NamedResource):
    areas: List[MinimalResource["LocationArea"]]
    game_indices: List["GenerationGameIndex"]
    region: MinimalResource["Region"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.areas = [MinimalResource(area_data) for area_data in data["areas"]]
        self.game_indices = [GenerationGameIndex(game_indice_data) for game_indice_data in data["game_indices"]]
        self.region = MinimalResource(data["region"])
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<Location areas={self.areas} game_indices={self.game_indices} id_={self.id_} region={self.region} name='{self.name}' names={self.names}>"
