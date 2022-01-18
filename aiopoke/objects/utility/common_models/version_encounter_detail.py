from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility.common_models.encounter import Encounter
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Version


class VersionEncounterDetail(Resource):
    encounter_details: Tuple["Encounter", ...]
    max_chance: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.encounter_details = tuple(
            Encounter(encounter_details_data)
            for encounter_details_data in data["encounter_details"]
        )
        self.max_chance = data["max_chance"]
        self.version = MinimalResource(data["version"])
