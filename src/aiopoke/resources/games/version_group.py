from typing import List
from ...minimal_resources import (
    MinimalGeneration,
    MinimalRegion,
    MinimalPokedex,
    MinimalMoveLearnMethod,
    MinimalVersion,
    MinimalVersionGroup,
)
from ...utility import NamedResource


class VersionGroup(NamedResource):
    generation: "MinimalGeneration"
    move_learn_methods: List["MinimalMoveLearnMethod"]
    order: int
    pokedexes: List["MinimalPokedex"]
    regions: List["MinimalRegion"]
    versions: List["MinimalVersion"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.generation = MinimalGeneration(data["generation"])
        self.move_learn_methods = [
            MinimalMoveLearnMethod(move_learn_method_data)
            for move_learn_method_data in data["move_learn_methods"]
        ]
        self.order = data["order"]
        self.pokedexes = [
            MinimalPokedex(pokedex_data) for pokedex_data in data["pokedexes"]
        ]
        self.regions = [MinimalRegion(region_data) for region_data in data["regions"]]
        self.versions = [
            MinimalVersion(version_data) for version_data in data["versions"]
        ]

    def __repr__(self) -> str:
        return (
            f"<VersionGroup generation={self.generation} move_learn_methods={self.move_learn_methods} "
            f"order={self.order} pokedexes={self.pokedexes} regions={self.regions} versions={self.versions}>"
        )


class VersionGroupDetail:
    level_learned_at: int
    move_learn_method: "MinimalMoveLearnMethod"
    version_group: "MinimalVersionGroup"

    def __init__(self, data) -> None:
        self.level_learned_at = data["level_learned_at"]
        self.move_learn_method = MinimalMoveLearnMethod(data["move_learn_method"])
        self.version_group = MinimalVersionGroup(data["version_group"])

    def __repr__(self) -> str:
        return f"<VersionGroupDetail level_learned_at={self.level_learned_at} move_learn_method={self.move_learn_method} version_group={self.version_group}>"
