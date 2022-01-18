from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Generation, Pokedex, VersionGroup
    from aiopoke.objects.resources.locations import Location


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
        self.pokedexes = [
            MinimalResource(pokedex_data) for pokedex_data in data["pokedexes"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.version_groups = [
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        ]
