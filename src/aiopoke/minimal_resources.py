from typing import TYPE_CHECKING, Coroutine, Generic, TypeVar, Dict, Callable, Any, Union


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

        build_map: Dict[str, Callable[[], Callable[[Union[str, int]], Coroutine[Any, Any, Any]]]] = {
            "ability": lambda: client.fetch_ability,
            "berry": lambda: client.fetch_berry,
            "berry-firmness": lambda: client.fetch_berry_firmness,
            "berry-flavor": lambda: client.fetch_berry_flavor,
            "characteristic": lambda: client.fetch_characteristic,
            "contest-effect": lambda: client.fetch_contest_effect,
            "contest-type": lambda: client.fetch_contest_type,
            "egg-group": lambda: client.fetch_egg_group,
            "encounter-condition": lambda: client.fetch_encounter_condition,
            "encounter-condition-value": lambda: client.fetch_encounter_condition_value,
            "encounter-method": lambda: client.fetch_encounter_method,
            "evolution-chain": lambda: client.fetch_evolution_chain,
            "evolution-trigger": lambda: client.fetch_evolution_trigger,
            "gender": lambda: client.fetch_gender,
            "generation": lambda: client.fetch_generation,
            "growth-rate": lambda: client.fetch_growth_rate,
            "item": lambda: client.fetch_item,
            "item-attribute": lambda: client.fetch_item_attribute,
            "item-category": lambda: client.fetch_item_category,
            "item-fling-effect": lambda: client.fetch_item_fling_effect,
            "item-pocket": lambda: client.fetch_item_pocket,
            "language": lambda: client.fetch_language,
            "location": lambda: client.fetch_location,
            "location-area": lambda: client.fetch_location_area,
            "machine": lambda: client.fetch_machine,
            "move": lambda: client.fetch_move,
            "move-ailment": lambda: client.fetch_move_ailment,
            "move-battle-style": lambda: client.fetch_move_battle_style,
            "move-category": lambda: client.fetch_move_category,
            "move-damage-class": lambda: client.fetch_move_damage_class,
            "move-learn-method": lambda: client.fetch_move_learn_method,
            "move-target": lambda: client.fetch_move_target,
            "nature": lambda: client.fetch_nature,
            "pal-park-area": lambda: client.fetch_pal_park_area,
            "pokeathlon-stat": lambda: client.fetch_pokeathlon_stat,
            "pokedex": lambda: client.fetch_pokedex,
            "pokemon": lambda: client.fetch_pokemon,
            "pokemon-color": lambda: client.fetch_pokemon_color,
            "pokemon-form": lambda: client.fetch_pokemon_form,
            "pokemon-habitat": lambda: client.fetch_pokemon_habitat,
            "pokemon-shape": lambda: client.fetch_pokemon_shape,
            "pokemon-species": lambda: client.fetch_pokemon_species,
            "region": lambda: client.fetch_region,
            "stat": lambda: client.fetch_stat,
            "super-contest-effect": lambda: client.fetch_super_contest_effect,
            "type": lambda: client.fetch_natural_gift_type,
            "version": lambda: client.fetch_version,
            "version-group": lambda: client.fetch_version_group,
        }

        obj: T = await build_map[self.endpoint]()(self.id_)
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
