from typing import TYPE_CHECKING, List

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

    def __init__(self, data) -> None:
        super().__init__(data)
        self.effect_changes = [
            AbilityEffectChange(effect_change_data)
            for effect_change_data in data["effect_changes"]
        ]
        self.effect_entries = [
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        ]
        self.flavor_text_entries = [
            AbilityFlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.generation = MinimalResource(data["generation"])
        self.is_main_series = data["is_main_series"]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.pokemon = [
            AbilityPokemon(pokemon_data) for pokemon_data in data["pokemon"]
        ]


class AbilityPokemon(Resource):
    is_hidden: bool
    slot: int
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, data) -> None:
        self.is_hidden = data["is_hidden"]
        self.slot = data["slot"]
        self.pokemon = MinimalResource(data["pokemon"])


class AbilityEffectChange(Resource):
    effect_entries: List["Effect"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.effect_entries = [
            Effect(effect_entry_data) for effect_entry_data in data["effect_entries"]
        ]
        self.version_group = MinimalResource(data["version_group"])


class AbilityFlavorText:
    flavor_text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalResource(data["language"])
        self.version_group = MinimalResource(data["version_group"])
