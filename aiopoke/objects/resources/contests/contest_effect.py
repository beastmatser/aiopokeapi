from typing import Tuple

from aiopoke.objects.utility import Effect
from aiopoke.objects.utility import FlavorText
from aiopoke.utils.resource import Resource


class ContestEffect(Resource):
    appeal: int
    effect_entry: "Effect"
    effect_entries: Tuple["Effect", ...]
    flavor_text_entry: "FlavorText"
    flavor_text_entries: Tuple["FlavorText", ...]
    id_: int
    jam: int

    def __init__(self, data) -> None:
        self.appeal = data["appeal"]
        self.effect_entry = tuple(
            Effect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        )[0]
        self.effect_entries = tuple(
            Effect(effect_entry_data) for effect_entry_data in data["effect_entries"]
        )
        self.flavor_text_entry = tuple(
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        )[0]
        self.flavor_text_entries = tuple(
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        )
        self.id_ = data["id"]
        self.jam = data["jam"]
