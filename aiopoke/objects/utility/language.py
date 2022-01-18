from typing import List

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource


class Language(NamedResource):
    official: bool
    iso3166: str
    iso639: str
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.official = data["official"]
        self.iso639 = data["iso639"]
        self.iso3166 = data["iso3166"]
        self.names = [Name(name_data) for name_data in data["names"]]
