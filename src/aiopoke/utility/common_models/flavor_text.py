from typing import Optional
from ...minimal_resources import MinimalLanguage, MinimalVersion


class FlavorText:
    flavor_text: str
    language: "MinimalLanguage"
    version: Optional["MinimalVersion"]

    def __init__(self, data) -> None:
        self.flavor_text = data["flavor_text"]
        self.language = MinimalLanguage(data["language"])
        self.version = MinimalVersion(data["version"]) if data.get("version") is not None else None

    def __repr__(self) -> str:
        return f"<FlavorText flavor_text='{self.flavor_text}' language={self.language} version={self.version}>"
