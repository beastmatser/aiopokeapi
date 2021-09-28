from typing import List
from ...utility import Effect, FlavorText


class ContestEffect:
    appeal: int
    effect_entry: "Effect"
    effect_entries: List["Effect"]
    flavor_text_entry: "FlavorText"
    flavor_text_entries: List["FlavorText"]
    id_: int
    jam: int

    def __init__(self, data) -> None:
        self.appeal = data["appeal"]
        self.effect_entry = [
            Effect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        ][0]
        self.effect_entries = [
            Effect(effect_entry_data) for effect_entry_data in data["effect_entries"]
        ]
        self.flavor_text_entry = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        ][0]
        self.flavor_text_entries = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.id_ = data["id"]
        self.jam = data["jam"]

    def __repr__(self) -> str:
        return (
            f"<ContestEffect appeal={self.appeal} effect_entry={self.effect_entry} "
            f"effect_entries={self.effect_entries} flavor_text_entry={self.flavor_text_entry} "
            f"flavor_text_entries={self.flavor_text_entries} id_={self.id_} jam={self.jam}>"
        )
