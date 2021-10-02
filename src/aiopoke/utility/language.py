from typing import Tuple

from .common_models import Name, NamedResource


class Language(NamedResource):
    official: bool
    iso3166: str
    iso639: str
    names: Tuple["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.official = data["official"]
        self.iso639 = data["iso639"]
        self.iso3166 = data["iso3166"]
        self.names = tuple(Name(name_data) for name_data in data["names"])

    def __repr__(self) -> str:
        return (
            f"<Language id_={self.id_} official={self.official} iso3166={self.iso3166} iso639={self.iso639} "
            f"name='{self.name}' names={self.names}>"
        )
