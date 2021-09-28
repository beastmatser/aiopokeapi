from ...minimal_resources import MinimalLanguage, MinimalVersion


class FlavorText:
    flavor_text: str
    language: "MinimalLanguage"
    version: "MinimalVersion"

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalLanguage(data["language"])
        self.version = MinimalVersion(data["version"])

    def __repr__(self) -> str:
        return f"<FlavorText flavor_text='{self.flavor_text}' language={self.language} version={self.version}>"
