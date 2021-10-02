class NamedResource:
    """A resource with a name and id"""

    name: str
    id_: int

    def __init__(self, data) -> None:
        self.name = data["name"]
        self.id_ = data["id"]

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, self.__class__)
            and other.name == self.name
            and other.id_ == self.id_
        )
