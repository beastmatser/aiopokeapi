from ...minimal_resources import MinimalVersionGroup, MinimalLanguage


class VersionGroupFlavorText:
    text: str
    language: "MinimalLanguage"
    version_group: "MinimalVersionGroup"

    def __init__(self, data) -> None:
        self.text = data["text"]
        self.language = MinimalLanguage(data["language"])
        self.version_group = MinimalVersionGroup(data["version_group"])

    def __repr__(self) -> str:
        return f"<VersionGroupFlavorText text='{self.text}' language={self.language} version_group={self.version_group}>"
