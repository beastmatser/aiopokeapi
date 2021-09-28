from typing import List
from ...minimal_resources import MinimalVersion
from .encounter import Encounter


class VersionEncounterDetail:
    encounter_details: List["Encounter"]
    max_chance: int
    version: "MinimalVersion"

    def __init__(self, data) -> None:
        self.encounter_details = [
            Encounter(encounter_details_data)
            for encounter_details_data in data["encounter_details"]
        ]
        self.max_chance = data["max_chance"]
        self.version = MinimalVersion(data["version"])

    def __repr__(self) -> str:
        return f"<VersionEncounterDetail encounter_details={self.encounter_details} max_change={self.max_chance} version={self.version}>"
