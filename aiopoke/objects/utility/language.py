from typing import List, Dict, Any

from aiopoke.objects.utility.common_models import Name, NamedResource


class Language(NamedResource):
    official: bool
    iso3166: str
    iso639: str
    names: List["Name"]

    def __init__(
        self, *, official: bool, iso3166: str, iso639: str, names: List[Dict[str, Any]]
    ):
        self.official = official
        self.iso3166 = iso3166
        self.iso639 = iso639
        self.names = [Name(**name) for name in names]
