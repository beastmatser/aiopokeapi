from aiopoke.utils.resource import Resource


class NamedResource(Resource):
    """A resource with a name and id"""

    name: str
    id: int

    def __init__(self, *, name: str, id: int):
        self.name = name
        self.id = id

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, self.__class__)
            and other.name == self.name
            and other.id == self.id
        )
