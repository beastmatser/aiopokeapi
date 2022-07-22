from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.resources.games.version import Version
from aiopoke.objects.utility import NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import MoveLearnMethod, Pokedex, Region


class VersionGroup(NamedResource):
    generation: MinimalResource["Region"]
    move_learn_methods: List[MinimalResource["MoveLearnMethod"]]
    order: int
    pokedexes: List[MinimalResource["Pokedex"]]
    regions: List[MinimalResource["Region"]]
    versions: List[MinimalResource["Version"]]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        generation: Dict[str, Any],
        move_learn_methods: List[Dict[str, Any]],
        order: int,
        pokedexes: List[Dict[str, Any]],
        regions: List[Dict[str, Any]],
        versions: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.generation = MinimalResource(**generation)
        self.move_learn_methods = [
            MinimalResource(**move_learn_method)
            for move_learn_method in move_learn_methods
        ]
        self.order = order
        self.pokedexes = [MinimalResource(**pokedex) for pokedex in pokedexes]
        self.regions = [MinimalResource(**region) for region in regions]
        self.versions = [MinimalResource(**version) for version in versions]


class VersionGroupDetail(Resource):
    level_learned_at: int
    move_learn_method: MinimalResource["MoveLearnMethod"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self,
        *,
        level_learned_at: int,
        move_learn_method: Dict[str, Any],
        version_group: Dict[str, Any],
    ) -> None:
        self.level_learned_at = level_learned_at
        self.move_learn_method = MinimalResource(**move_learn_method)
        self.version_group = MinimalResource(**version_group)
