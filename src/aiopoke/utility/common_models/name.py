from ...minimal_resources import MinimalLanguage


class Name:
    name: str
    language: "MinimalLanguage"

    def __init__(self, data) -> None:
        self.name = data["name"]
        self.language = MinimalLanguage(data["language"])

    def __repr__(self) -> str:
        return f"<Name name='{self.name}' language={self.language}>"
