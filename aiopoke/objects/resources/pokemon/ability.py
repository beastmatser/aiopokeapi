from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import Effect, NamedResource, VerboseEffect
from aiopoke.objects.utility.common_models import Name
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Generation, VersionGroup
    from aiopoke.objects.resources.pokemon import Pokemon
    from aiopoke.objects.utility import Language


class Ability(NamedResource):
    effect_changes: List["AbilityEffectChange"]
    effect_entries: List["VerboseEffect"]
    flavor_text_entries: List["AbilityFlavorText"]
    generation: MinimalResource["Generation"]
    is_main_series: bool
    names: List["Name"]
    pokemon: List["AbilityPokemon"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        effect_changes: List[Dict[str, Any]],
        effect_entries: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
        generation: Dict[str, Any],
        is_main_series: bool,
        names: List[Dict[str, Any]],
        pokemon: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.effect_changes = [
            AbilityEffectChange(**effect_change) for effect_change in effect_changes
        ]
        self.effect_entries = [
            VerboseEffect(**effect_entry) for effect_entry in effect_entries
        ]
        self.flavor_text_entries = [
            AbilityFlavorText(**flavor_text_entry)
            for flavor_text_entry in flavor_text_entries
        ]
        self.generation = MinimalResource(**generation)
        self.is_main_series = is_main_series
        self.names = [Name(**name) for name in names]
        self.pokemon = [AbilityPokemon(**pokemon) for pokemon in pokemon]


class AbilityPokemon(Resource):
    is_hidden: bool
    slot: int
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, *, is_hidden: bool, slot: int, pokemon: Dict[str, Any]) -> None:
        self.is_hidden = is_hidden
        self.slot = slot
        self.pokemon = MinimalResource(**pokemon)


class AbilityEffectChange(Resource):
    effect_entries: List["Effect"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self, *, effect_entries: List[Dict[str, Any]], version_group: Dict[str, Any]
    ) -> None:
        self.effect_entries = [
            Effect(**effect_entry) for effect_entry in effect_entries
        ]
        self.version_group = MinimalResource(**version_group)


class AbilityFlavorText(Resource):
    flavor_text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(
        self,
        *,
        flavor_text: str,
        language: Dict[str, Any],
        version_group: Dict[str, Any],
    ) -> None:
        self.flavor_text = flavor_text
        self.language = MinimalResource(**language)
        self.version_group = MinimalResource(**version_group)
