from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Generation, Pokedex, VersionGroup
    from aiopoke.objects.resources.locations import Location


class Region(NamedResource):
    locations: Tuple[MinimalResource["Location"], ...]
    main_generation: MinimalResource["Generation"]
    pokedexes: Tuple[MinimalResource["Pokedex"], ...]
    names: Tuple["Name", ...]
    version_groups: Tuple[MinimalResource["VersionGroup"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.locations = tuple(
            MinimalResource(location_data) for location_data in data["locations"]
        )
        self.main_generation = MinimalResource(data["main_generation"])
        self.pokedexes = tuple(
            MinimalResource(pokedex_data) for pokedex_data in data["pokedexes"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.version_groups = tuple(
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        )
