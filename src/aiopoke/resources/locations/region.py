from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility import Name, NamedResource

if TYPE_CHECKING:
    from . import Location
    from ...resources import Generation, Pokedex, VersionGroup


class Region(NamedResource):
    locations: List[MinimalResource["Location"]]
    main_generation: MinimalResource["Generation"]
    pokedexes: List[MinimalResource["Pokedex"]]
    names: List["Name"]
    version_groups: List[MinimalResource["VersionGroup"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.locations = [
            MinimalResource(location_data) for location_data in data["locations"]
        ]
        self.main_generation = MinimalResource(data["main_generation"])
        self.pokedexes = [MinimalResource(pokedex_data) for pokedex_data in data["pokedexes"]]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.version_groups = [MinimalResource(version_group_data) for version_group_data in data["version_groups"]]

    def __repr__(self) -> str:
        return (
            f"<Region id_={self.id_} locations={self.locations} main_generation={self.main_generation} "
            f"pokedexes={self.pokedexes} name='{self.name}' names={self.names} version_groups={self.version_groups}>"
        )
