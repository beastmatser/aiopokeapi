from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import Nature


class PokeathlonStat(NamedResource):
    affecting_natures: "NaturePokeathlonStatAffectSets"
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.affecting_natures = NaturePokeathlonStatAffectSets(
            data["affecting_natures"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])


class NaturePokeathlonStatAffectSets(Resource):
    increase: Tuple["NaturePokeathlonStatAffect", ...]
    decrease: Tuple["NaturePokeathlonStatAffect", ...]

    def __init__(self, data) -> None:
        self.increase = tuple(
            NaturePokeathlonStatAffect(increase_data)
            for increase_data in data["increase"]
        )
        self.decrease = tuple(
            NaturePokeathlonStatAffect(decrease_data)
            for decrease_data in data["decrease"]
        )


class NaturePokeathlonStatAffect(Resource):
    max_change: int
    nature: MinimalResource["Nature"]

    def __init__(self, data) -> None:
        self.max_change = data["max_change"]
        self.nature = MinimalResource(data["nature"])
