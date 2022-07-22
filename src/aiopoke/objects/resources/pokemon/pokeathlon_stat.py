from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import Nature


class PokeathlonStat(NamedResource):
    affecting_natures: "NaturePokeathlonStatAffectSets"
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        affecting_natures: Dict[str, Any],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.affecting_natures = NaturePokeathlonStatAffectSets(**affecting_natures)
        self.names = [Name(**name) for name in names]


class NaturePokeathlonStatAffectSets(Resource):
    increase: List["NaturePokeathlonStatAffect"]
    decrease: List["NaturePokeathlonStatAffect"]

    def __init__(
        self, *, increase: List[Dict[str, Any]], decrease: List[Dict[str, Any]]
    ) -> None:
        self.increase = [
            NaturePokeathlonStatAffect(**increase_data) for increase_data in increase
        ]
        self.decrease = [
            NaturePokeathlonStatAffect(**decrease_data) for decrease_data in decrease
        ]


class NaturePokeathlonStatAffect(Resource):
    max_change: int
    nature: MinimalResource["Nature"]

    def __init__(
        self,
        *,
        max_change: int,
        nature: Dict[str, Any],
    ) -> None:
        self.max_change = max_change
        self.nature = MinimalResource(**nature)
