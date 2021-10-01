from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from .resources import Pokemon


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


class MinimalPokemon(MinimalResource["Pokemon"]):
    async def fetch(self) -> "Pokemon":
        from .aiopoke_client import AiopokeClient  # type: ignore

        client = AiopokeClient()  # this will return an existing instance

        data = await client._fetch(self.endpoint, self.id_)
        response = await client.session.get(f"https://pokeapi.co/api/v2/pokemon/{self.id_}/encounters")  # type: ignore
        data["location_area_encounters"] = await response.json()
        obj: "Pokemon" = client.build(self.endpoint, data)
        return obj
