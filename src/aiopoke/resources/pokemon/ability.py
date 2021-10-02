from typing import TYPE_CHECKING, Tuple

from ...minimal_resources import MinimalResource
from ...utility import Effect, NamedResource, VerboseEffect
from ...utility.common_models import Name

if TYPE_CHECKING:
    from ...resources import Generation, VersionGroup
    from ...utility import Language
    from . import Pokemon


class Ability(NamedResource):
    effect_changes: Tuple["AbilityEffectChange"]
    effect_entry: "VerboseEffect"
    effect_entries: Tuple["VerboseEffect"]
    flavor_text_entry: "AbilityFlavorText"
    flavor_text_entries: Tuple["AbilityFlavorText"]
    generation: MinimalResource["Generation"]
    is_main_series: bool
    names: Tuple["Name"]
    pokemon: Tuple["AbilityPokemon"]

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

    def __repr__(self) -> str:
        return (
            f"<Ability effect_changes={self.effect_changes} effect_entries={self.effect_entries} "
            f"flavor_text_entries={self.flavor_text_entries} generation={self.generation}"
            f"id_={self.id_} is_main_series={self.is_main_series} name='{self.name}' pokemon={self.pokemon}"
        )


class AbilityPokemon:
    is_hidden: bool
    slot: int
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, data) -> None:
        self.is_hidden = data["is_hidden"]
        self.slot = data["slot"]
        self.pokemon = MinimalResource(data["pokemon"])

    def __repr__(self) -> str:
        return f"<AbilityPokemon is_hidden={self.is_hidden} slot={self.slot} pokemon={self.pokemon}>"


class AbilityEffectChange:
    effect_entry: "Effect"
    effect_entries: Tuple["Effect"]
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

    def __repr__(self) -> str:
        return f"<AbilityEffectChange effect_entry={self.effect_entry} effect_entries={self.effect_entries} version_group={self.version_group}>"


class AbilityFlavorText:
    flavor_text: str
    language: MinimalResource["Language"]
    version_group: MinimalResource["VersionGroup"]

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalResource(data["language"])
        self.version_group = MinimalResource(data["version_group"])

    def __repr__(self) -> str:
        return f"<AbilityFlavorText flavor_text={self.flavor_text} language={self.language} version_group={self.version_group}>"
