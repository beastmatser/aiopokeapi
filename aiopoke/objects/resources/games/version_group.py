from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.resources.games.version import Version
from aiopoke.objects.utility import NamedResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import MoveLearnMethod, Pokedex, Region


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


class VersionGroupDetail(Resource):
    level_learned_at: int
    move_learn_method: MinimalResource["MoveLearnMethod"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.level_learned_at = data["level_learned_at"]
        self.move_learn_method = MinimalResource(data["move_learn_method"])
        self.version_group = MinimalResource(data["version_group"])
