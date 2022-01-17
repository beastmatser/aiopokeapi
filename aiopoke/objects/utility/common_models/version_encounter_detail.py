from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from .encounter import Encounter

if TYPE_CHECKING:
    from ...resources import Version


class VersionEncounterDetail:
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

    def __repr__(self) -> str:
        return f"<VersionEncounterDetail encounter_details={self.encounter_details} max_change={self.max_chance} version={self.version}>"
