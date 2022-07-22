from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import Name, NamedResource
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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        locations: List[Dict[str, Any]],
        main_generation: Dict[str, Any],
        pokedexes: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        version_groups: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.locations = [MinimalResource(**location) for location in locations]
        self.main_generation = MinimalResource(**main_generation)
        self.pokedexes = [MinimalResource(**pokedex) for pokedex in pokedexes]
        self.names = [Name(**name) for name in names]
        self.version_groups = [
            MinimalResource(**version_group) for version_group in version_groups
        ]
