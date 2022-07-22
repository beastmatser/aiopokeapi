from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility.common_models.encounter import Encounter
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Version


class VersionEncounterDetail(Resource):
    encounter_details: List["Encounter"]
    max_chance: int
    version: MinimalResource["Version"]

    def __init__(
        self,
        *,
        encounter_details: List[Dict[str, Any]],
        max_chance: int,
        version: Dict[str, Any]
    ):
        self.encounter_details = [
            Encounter(**encounter_detail) for encounter_detail in encounter_details
        ]
        self.max_chance = max_chance
        self.version = MinimalResource(**version)
