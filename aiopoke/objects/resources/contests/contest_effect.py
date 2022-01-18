from typing import List

from aiopoke.objects.utility import Effect
from aiopoke.objects.utility import FlavorText
from aiopoke.utils.resource import Resource


class ContestEffect(Resource):
    appeal: int
    effect_entries: List["Effect"]
    flavor_text_entries: List["FlavorText"]
    id_: int
    jam: int

    def __init__(self, data) -> None:
        self.appeal = data["appeal"]
        self.effect_entries = [
            Effect(effect_entry_data) for effect_entry_data in data["effect_entries"]
        ]
        self.flavor_text_entries = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.id_ = data["id"]
        self.jam = data["jam"]
