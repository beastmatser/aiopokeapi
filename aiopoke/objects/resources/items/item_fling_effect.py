from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Effect
from aiopoke.objects.utility import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.items import Item


class ItemFlingEffect(NamedResource):
    effect_entry: "Effect"
    effect_entries: Tuple["Effect", ...]
    items: Tuple[MinimalResource["Item"], ...]

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
