from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Dict,
    Generic,
    TypeVar,
    Union,
)

if TYPE_CHECKING:
    from .aiopoke_client import AiopokeClient

T = TypeVar("T")
U = TypeVar("U")


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

    async def fetch(self, client: "AiopokeClient") -> T:
        build_map: Dict[str, Callable[[Union[str, int]], Coroutine[Any, Any, Any]]] = {
            "ability": client.fetch_ability,
            "berry": client.fetch_berry,
            "berry-firmness": client.fetch_berry_firmness,
            "berry-flavor": client.fetch_berry_flavor,
            "characteristic": client.fetch_characteristic,
            "contest-effect": client.fetch_contest_effect,
            "contest-type": client.fetch_contest_type,
            "egg-group": client.fetch_egg_group,
            "encounter-condition": client.fetch_encounter_condition,
            "encounter-condition-value": client.fetch_encounter_condition_value,
            "encounter-method": client.fetch_encounter_method,
            "evolution-chain": client.fetch_evolution_chain,
            "evolution-trigger": client.fetch_evolution_trigger,
            "gender": client.fetch_gender,
            "generation": client.fetch_generation,
            "growth-rate": client.fetch_growth_rate,
            "item": client.fetch_item,
            "item-attribute": client.fetch_item_attribute,
            "item-category": client.fetch_item_category,
            "item-fling-effect": client.fetch_item_fling_effect,
            "item-pocket": client.fetch_item_pocket,
            "language": client.fetch_language,
            "location": client.fetch_location,
            "location-area": client.fetch_location_area,
            "machine": client.fetch_machine,
            "move": client.fetch_move,
            "move-ailment": client.fetch_move_ailment,
            "move-battle-style": client.fetch_move_battle_style,
            "move-category": client.fetch_move_category,
            "move-damage-class": client.fetch_move_damage_class,
            "move-learn-method": client.fetch_move_learn_method,
            "move-target": client.fetch_move_target,
            "nature": client.fetch_nature,
            "pal-park-area": client.fetch_pal_park_area,
            "pokeathlon-stat": client.fetch_pokeathlon_stat,
            "pokedex": client.fetch_pokedex,
            "pokemon": client.fetch_pokemon,
            "pokemon-color": client.fetch_pokemon_color,
            "pokemon-form": client.fetch_pokemon_form,
            "pokemon-habitat": client.fetch_pokemon_habitat,
            "pokemon-shape": client.fetch_pokemon_shape,
            "pokemon-species": client.fetch_pokemon_species,
            "region": client.fetch_region,
            "stat": client.fetch_stat,
            "super-contest-effect": client.fetch_super_contest_effect,
            "type": client.fetch_natural_gift_type,
            "version": client.fetch_version,
            "version-group": client.fetch_version_group,
        }

        obj: T = await build_map[self.endpoint](self.id_)
        return obj


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
