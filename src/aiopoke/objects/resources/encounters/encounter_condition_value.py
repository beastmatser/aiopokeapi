from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.encounters import EncounterCondition


class EncounterConditionValue(NamedResource):
    condition: MinimalResource["EncounterCondition"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        condition: Dict[str, Any],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.condition = MinimalResource(**condition)
        self.names = [Name(**name) for name in names]
