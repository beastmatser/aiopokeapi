from typing import List
from ...minimal_resources import MinimalItem
from ...utility import Effect, NamedResource


class ItemFlingEffect(NamedResource):
    effect_entry: "Effect"
    effect_entries: List["Effect"]
    items: List["MinimalItem"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.items = [MinimalItem(item_data) for item_data in data["items"]]
        self.effect_entry = [
            Effect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        ][0]
        self.effect_entries = [
            Effect(effect_entry_data) for effect_entry_data in data["effect_entries"]
        ]

    def __repr__(self) -> str:
        return f"<ItemFlingEffect effect_entry={self.effect_entry} effect_entries={self.effect_entries} id_={self.id_} items={self.items} name='{self.name}'>"
