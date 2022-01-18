from typing import TYPE_CHECKING, List, Dict, Any

from aiopoke.objects.utility import Effect, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.items import Item


class ItemFlingEffect(NamedResource):
    effect_entries: List["Effect"]
    items: List[MinimalResource["Item"]]

    def __init__(
        self,
        *,
        effect_entries: List[Dict[str, Any]],
        items: List[Dict[str, Any]],
    ) -> None:
        self.effect_entries = [
            Effect(**effect_entry) for effect_entry in effect_entries
        ]
        self.items = [MinimalResource(**item) for item in items]
