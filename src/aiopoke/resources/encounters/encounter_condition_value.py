from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from . import EncounterCondition


class EncounterConditionValue(NamedResource):
    condition: MinimalResource["EncounterCondition"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.condition = MinimalResource(data["condition"])
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<EncounterConditionValue condition={self.condition} id_={self.id_} name='{self.name}' names={self.names}>"
