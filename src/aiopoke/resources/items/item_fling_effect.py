from typing import TYPE_CHECKING, Tuple

from ...minimal_resources import MinimalResource
from ...utility import Effect, NamedResource

if TYPE_CHECKING:
    from . import Item


class ItemFlingEffect(NamedResource):
    effect_entry: "Effect"
    effect_entries: Tuple["Effect"]
    items: Tuple[MinimalResource["Item"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.items = tuple(MinimalResource(item_data) for item_data in data["items"])
        self.effect_entry = tuple(
            Effect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        )[0]
        self.effect_entries = tuple(
            Effect(effect_entry_data) for effect_entry_data in data["effect_entries"]
        )

    def __repr__(self) -> str:
        return f"<ItemFlingEffect effect_entry={self.effect_entry} effect_entries={self.effect_entries} id_={self.id_} items={self.items} name='{self.name}'>"
