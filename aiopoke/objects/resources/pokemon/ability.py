from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Effect
from aiopoke.objects.utility import NamedResource
from aiopoke.objects.utility import VerboseEffect
from aiopoke.objects.utility.common_models import Name
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Generation, VersionGroup
    from aiopoke.objects.utility import Language
    from aiopoke.objects.resources.pokemon import Pokemon


class Ability(NamedResource):
    effect_changes: Tuple["AbilityEffectChange", ...]
    effect_entry: "VerboseEffect"
    effect_entries: Tuple["VerboseEffect", ...]
    flavor_text_entry: "AbilityFlavorText"
    flavor_text_entries: Tuple["AbilityFlavorText", ...]
    generation: MinimalResource["Generation"]
    is_main_series: bool
    names: Tuple["Name", ...]
    pokemon: Tuple["AbilityPokemon", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.effect_changes = tuple(
            AbilityEffectChange(effect_change_data)
            for effect_change_data in data["effect_changes"]
        )
        self.effect_entry = tuple(
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        )[0]
        self.effect_entries = tuple(
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        )
        self.flavor_text_entry = tuple(
            AbilityFlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        )[0]
        self.flavor_text_entries = tuple(
            AbilityFlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        )
        self.generation = MinimalResource(data["generation"])
        self.is_main_series = data["is_main_series"]
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.pokemon = tuple(
            AbilityPokemon(pokemon_data) for pokemon_data in data["pokemon"]
        )


class AbilityPokemon(Resource):
    is_hidden: bool
    slot: int
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, data) -> None:
        self.is_hidden = data["is_hidden"]
        self.slot = data["slot"]
        self.pokemon = MinimalResource(data["pokemon"])


class AbilityEffectChange(Resource):
    effect_entry: "Effect"
    effect_entries: Tuple["Effect", ...]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.effect_entry = tuple(
            Effect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        )[0]
        self.effect_entries = tuple(
            Effect(effect_entry_data) for effect_entry_data in data["effect_entries"]
        )
        self.version_group = MinimalResource(data["version_group"])


class AbilityFlavorText:
    flavor_text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalResource(data["language"])
        self.version_group = MinimalResource(data["version_group"])
