from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.encounters import EncounterConditionValue


class EncounterCondition(NamedResource):
    values: List[MinimalResource["EncounterConditionValue"]]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        values: List[Dict[str, Any]],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.values = [MinimalResource(**value) for value in values]
        self.names = [Name(**name) for name in names]
