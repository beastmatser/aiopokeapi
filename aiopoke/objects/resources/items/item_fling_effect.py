from typing import TYPE_CHECKING, List

from aiopoke.objects.utility import Effect, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.items import Item


class ItemFlingEffect(NamedResource):
    effect_entries: List["Effect"]
    items: List[MinimalResource["Item"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.items = [MinimalResource(item_data) for item_data in data["items"]]
        self.effect_entries = [
            Effect(effect_entry_data) for effect_entry_data in data["effect_entries"]
        ]
