from typing import Any, Dict, List

from aiopoke.objects.utility import Effect, FlavorText
from aiopoke.utils.resource import Resource


class ContestEffect(Resource):
    appeal: int
    effect_entries: List["Effect"]
    flavor_text_entries: List["FlavorText"]
    id: int
    jam: int

    def __init__(
        self,
        *,
        id: int,
        appeal: int,
        effect_entries: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
        jam: int
    ) -> None:
        self.id = id
        self.appeal = appeal
        self.effect_entries = [Effect(**effect) for effect in effect_entries]
        self.flavor_text_entries = [
            FlavorText(**flavor) for flavor in flavor_text_entries
        ]
        self.jam = jam
