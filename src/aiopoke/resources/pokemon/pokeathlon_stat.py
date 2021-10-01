from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from . import Nature


class PokeathlonStat(NamedResource):
    affecting_natures: "NaturePokeathlonStatAffectSets"
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.affecting_natures = NaturePokeathlonStatAffectSets(data["affecting_natures"])
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<PokeathlonStat affecting_natures={self.affecting_natures} id_={self.id_} name='{self.name}' names={self.names}>"


class NaturePokeathlonStatAffectSets:
    increase: List["NaturePokeathlonStatAffect"]
    decrease: List["NaturePokeathlonStatAffect"]

    def __init__(self, data) -> None:
        self.increase = [NaturePokeathlonStatAffect(increase_data) for increase_data in data["increase"]]
        self.decrease = [NaturePokeathlonStatAffect(decrease_data) for decrease_data in data["decrease"]]

    def __repr__(self) -> str:
        return f"<NaturePokeathlonStatAffectSets increase={self.increase} decrease={self.decrease}>"


class NaturePokeathlonStatAffect:
    max_change: int
    nature: MinimalResource["Nature"]

    def __init__(self, data) -> None:
        self.max_change = data["max_change"]
        self.nature = MinimalResource(data["nature"])

    def __repr__(self) -> str:
        return f"<NaturePokeathlonStatAffect max_change={self.max_change} nature={self.nature}>"
