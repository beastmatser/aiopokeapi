from typing import TYPE_CHECKING, List

from aiopoke.objects.utility.common_models.encounter import Encounter
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Version


class VersionEncounterDetail(Resource):
    encounter_details: List["Encounter"]
    max_chance: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.encounter_details = [
            Encounter(encounter_details_data)
            for encounter_details_data in data["encounter_details"]
        ]
        self.max_chance = data["max_chance"]
        self.version = MinimalResource(data["version"])
