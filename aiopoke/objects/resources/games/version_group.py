from typing import Tuple
from typing import TYPE_CHECKING

from ...resources.games.version import Version

from ....minimal_resources import MinimalResource
from ...utility import NamedResource

if TYPE_CHECKING:
    from ...resources import MoveLearnMethod, Pokedex, Region


class VersionGroup(NamedResource):
    generation: MinimalResource["Region"]
    move_learn_methods: Tuple[MinimalResource["MoveLearnMethod"], ...]
    order: int
    pokedexes: Tuple[MinimalResource["Pokedex"], ...]
    regions: Tuple[MinimalResource["Region"], ...]
    versions: Tuple[MinimalResource["Version"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.generation = MinimalResource(data["generation"])
        self.move_learn_methods = tuple(
            MinimalResource(move_learn_method_data)
            for move_learn_method_data in data["move_learn_methods"]
        )
        self.order = data["order"]
        self.pokedexes = tuple(
            MinimalResource(pokedex_data) for pokedex_data in data["pokedexes"]
        )
        self.regions = tuple(
            MinimalResource(region_data) for region_data in data["regions"]
        )
        self.versions = tuple(
            MinimalResource(version_data) for version_data in data["versions"]
        )

    def __repr__(self) -> str:
        return (
            f"<VersionGroup generation={self.generation} move_learn_methods={self.move_learn_methods} "
            f"order={self.order} pokedexes={self.pokedexes} regions={self.regions} versions={self.versions}>"
        )


class VersionGroupDetail:
    level_learned_at: int
    move_learn_method: MinimalResource["MoveLearnMethod"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.level_learned_at = data["level_learned_at"]
        self.move_learn_method = MinimalResource(data["move_learn_method"])
        self.version_group = MinimalResource(data["version_group"])

    def __repr__(self) -> str:
        return f"<VersionGroupDetail level_learned_at={self.level_learned_at} move_learn_method={self.move_learn_method} version_group={self.version_group}>"
