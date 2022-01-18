from typing import TYPE_CHECKING, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.encounters import EncounterConditionValue


class EncounterCondition(NamedResource):
    values: List[MinimalResource["EncounterConditionValue"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.values = [
            MinimalResource(encounter_condition_value)
            for encounter_condition_value in data["values"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
