from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import Nature


class PokeathlonStat(NamedResource):
    affecting_natures: "NaturePokeathlonStatAffectSets"
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.affecting_natures = NaturePokeathlonStatAffectSets(
            data["affecting_natures"]
        )
        self.names = [Name(name_data) for name_data in data["names"]]


class NaturePokeathlonStatAffectSets(Resource):
    increase: List["NaturePokeathlonStatAffect"]
    decrease: List["NaturePokeathlonStatAffect"]

    def __init__(self, data) -> None:
        self.increase = [
            NaturePokeathlonStatAffect(increase_data)
            for increase_data in data["increase"]
        ]
        self.decrease = [
            NaturePokeathlonStatAffect(decrease_data)
            for decrease_data in data["decrease"]
        ]


class NaturePokeathlonStatAffect(Resource):
    max_change: int
    nature: MinimalResource["Nature"]

    def __init__(self, data) -> None:
        self.max_change = data["max_change"]
        self.nature = MinimalResource(data["nature"])
