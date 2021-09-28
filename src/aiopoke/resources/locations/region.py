from typing import List
from ...minimal_resources import MinimalLocation, MinimalGeneration, MinimalPokedex, MinimalVersionGroup
from ...utility import Name, NamedResource


class Region(NamedResource):
    locations: List["MinimalLocation"]
    main_generation: "MinimalGeneration"
    pokedexes: List["MinimalPokedex"]
    names: List["Name"]
    version_groups: List["MinimalVersionGroup"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.locations = [
            MinimalLocation(location_data) for location_data in data["locations"]
        ]
        self.main_generation = MinimalGeneration(data["main_generation"])
        self.pokedexes = [MinimalPokedex(pokedex_data) for pokedex_data in data["pokedexes"]]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.version_groups = [MinimalVersionGroup(version_group_data) for version_group_data in data["version_groups"]]

    def __repr__(self) -> str:
        return (
            f"<Region id_={self.id_} locations={self.locations} main_generation={self.main_generation} "
            f"pokedexes={self.pokedexes} name='{self.name}' names={self.names} version_groups={self.version_groups}>"
        )
