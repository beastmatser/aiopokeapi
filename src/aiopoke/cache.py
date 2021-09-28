from typing import Any, Callable, Coroutine, Dict, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from .aiopoke_client import AiopokeClient


# cache decorator
def cache(
    func,
) -> Callable[["AiopokeClient", str, Union[str, int]], Coroutine[Any, Any, Any]]:
    async def wrapper(
        client: "AiopokeClient", endpoint: str, name_or_id: Union[str, int]
    ) -> Union[Coroutine[Any, Any, Any], Any]:
        cached_item = client._cache.get(f"{endpoint}_{name_or_id}")
        if cached_item is not None:
            return cached_item

        data = await func(client, endpoint, name_or_id)
        if endpoint == "pokemon":
            response = await client.session.get(f"https://pokeapi.co/api/v2/pokemon/{name_or_id}/encounters")  # type: ignore
            data["location_area_encounters"] = await response.json()
        obj = client.build(endpoint, data)
        client._cache.put(f"{endpoint}", obj, data)
        return data

    return wrapper


class Cache:
    _cache: Dict[str, Any]
    _aliases: Dict[str, str]

    def __init__(self) -> None:
        self._cache = {}
        self._aliases = {}

    def get(self, name: str):
        cached_object = self._cache.get(name)
        if cached_object is not None:
            return cached_object

        cached_object_value = self._aliases.get(name)
        if cached_object_value is not None:
            cached_object_key = name.split("_")[0] + "_" + cached_object_value
            return self._cache[cached_object_key]

        return None

    def put(self, endpoint: str, obj: Any, data: Dict[str, Any]):
        self._cache[f"{endpoint.replace('-', '_')}_{obj.id_}"] = data
        if hasattr(obj, "name"):
            self._aliases[f"{endpoint}_{obj.name}"] = str(obj.id_)
