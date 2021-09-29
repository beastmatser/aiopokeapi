from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from .resources import (
        Ability,
        Berry,
        BerryFirmness,
        BerryFlavor,
        Characteristic,
        ContestType,
        ContestEffect,
        EggGroup,
        EncounterCondition,
        EncounterConditionValue,
        EncounterMethod,
        EvolutionChain,
        EvolutionTrigger,
        Generation,
        GrowthRate,
        Item,
        ItemAttribute,
        ItemCategory,
        ItemFlingEffect,
        ItemPocket,
        Location,
        LocationArea,
        Machine,
        Move,
        MoveAilment,
        MoveBatteStyle,
        MoveCategory,
        MoveDamageClass,
        MoveLearnMethod,
        NaturalGiftType,
        Nature,
        PalParkArea,
        PokeathlonStat,
        Pokedex,
        Pokemon,
        PokemonColor,
        PokemonForm,
        PokemonHabitat,
        PokemonShape,
        PokemonSpecies,
        Region,
        Stat,
        Version,
        VersionGroup,
    )
    from .utility.language import Language


T = TypeVar("T")


class Url(Generic[T]):
    url: str
    id_: int
    endpoint: str

    def __init__(self, data) -> None:
        self.url = data["url"]

        self.id_ = int(self.url.split("/")[-2])
        self.endpoint = self.url.split("/")[-3]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id_={self.id_} endpoint='{self.endpoint}'>"

    async def fetch(self) -> T:
        from .aiopoke_client import AiopokeClient  # type: ignore

        client = AiopokeClient()  # this will return an existing instance
        data = await client._fetch(self.endpoint, self.id_)
        obj: T = client.build(self.endpoint, data)
        return obj


class MachineUrl(Url["Machine"]):
    pass


class EvolutionChainUrl(Url["EvolutionChain"]):
    pass


class CharacteristicUrl(Url["Characteristic"]):
    pass


class ContestEffectUrl(Url["ContestEffect"]):
    pass


class MinimalResource(Url[T]):
    name: str
    url: str
    id_: int
    endpoint: str

    def __init__(self, data) -> None:
        super().__init__(data)
        self.name = data["name"]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}' id_={self.id_} endpoint='{self.endpoint}'>"


class MinimalAbility(MinimalResource["Ability"]):
    pass


class MinimalBerry(MinimalResource["Berry"]):
    pass


class MinimalBerryFirmness(MinimalResource["BerryFirmness"]):
    pass


class MinimalBerryFlavor(MinimalResource["BerryFlavor"]):
    pass


class MinimalContestType(MinimalResource["ContestType"]):
    pass


class MinimalEggGroup(MinimalResource["EggGroup"]):
    pass


class MinimalEncounterCondition(MinimalResource["EncounterCondition"]):
    pass


class MinimalEncounterConditionValue(MinimalResource["EncounterConditionValue"]):
    pass


class MinimalEncounterMethod(MinimalResource["EncounterMethod"]):
    pass


class MinimalEvolutionTrigger(MinimalResource["EvolutionTrigger"]):
    pass


class MinimalGeneration(MinimalResource["Generation"]):
    pass


class MinimalGrowthRate(MinimalResource["GrowthRate"]):
    pass


class MinimalItem(MinimalResource["Item"]):
    pass


class MinimalItemAttribute(MinimalResource["ItemAttribute"]):
    pass


class MinimalItemCategory(MinimalResource["ItemCategory"]):
    pass


class MinimalItemFlingEffect(MinimalResource["ItemFlingEffect"]):
    pass


class MinimalItemPocket(MinimalResource["ItemPocket"]):
    pass


class MinimalLanguage(MinimalResource["Language"]):
    pass


class MinimalLocation(MinimalResource["Location"]):
    pass


class MinimalLocationArea(MinimalResource["LocationArea"]):
    pass


class MinimalMove(MinimalResource["Move"]):
    pass


class MinimalMoveAilment(MinimalResource["MoveAilment"]):
    pass


class MinimalMoveBattleStyle(MinimalResource["MoveBatteStyle"]):
    pass


class MinimalMoveCategory(MinimalResource["MoveCategory"]):
    pass


class MinimalMoveDamageClass(MinimalResource["MoveDamageClass"]):
    pass


class MinimalMoveLearnMethod(MinimalResource["MoveLearnMethod"]):
    pass


class MinimalNaturalGiftType(MinimalResource["NaturalGiftType"]):
    pass


class MinimalNature(MinimalResource["Nature"]):
    pass


class MinimalParkPalArea(MinimalResource["PalParkArea"]):
    pass


class MinimalPokeathlonStat(MinimalResource["PokeathlonStat"]):
    pass


class MinimalPokedex(MinimalResource["Pokedex"]):
    pass


class MinimalPokemon(MinimalResource["Pokemon"]):
    async def fetch(self) -> "Pokemon":
        from .aiopoke_client import AiopokeClient  # type: ignore

        client = AiopokeClient()  # this will return an existing instance

        data = await client._fetch(self.endpoint, self.id_)
        response = await client.session.get(f"https://pokeapi.co/api/v2/pokemon/{self.id_}/encounters")  # type: ignore
        data["location_area_encounters"] = await response.json()
        obj: "Pokemon" = client.build(self.endpoint, data)
        return obj


class MinimalPokemonColor(MinimalResource["PokemonColor"]):
    pass


class MinimalPokemonForm(MinimalResource["PokemonForm"]):
    pass


class MinimalPokemonHabitat(MinimalResource["PokemonHabitat"]):
    pass


class MinimalPokemonShape(MinimalResource["PokemonShape"]):
    pass


class MinimalPokemonSpecies(MinimalResource["PokemonSpecies"]):
    pass


class MinimalRegion(MinimalResource["Region"]):
    pass


class MinimalStat(MinimalResource["Stat"]):
    pass


class MinimalVersion(MinimalResource["Version"]):
    pass


class MinimalVersionGroup(MinimalResource["VersionGroup"]):
    pass
