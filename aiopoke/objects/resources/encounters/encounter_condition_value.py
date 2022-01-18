from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.encounters import EncounterCondition


class EncounterConditionValue(NamedResource):
    condition: MinimalResource["EncounterCondition"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.condition = MinimalResource(data["condition"])
        self.names = [Name(name_data) for name_data in data["names"]]
