from ...minimal_resources import MinimalLanguage


class VerboseEffect:
    effect: str
    short_effect: str
    language: "MinimalLanguage"

    def __init__(self, data) -> None:
        self.effect = data["effect"]
        self.short_effect = data["short_effect"]
        self.language = MinimalLanguage(data["language"])

    def __repr__(self) -> str:
        return f"<VerboseEffect effect='{self.effect}' short_effect='{self.short_effect}' language={self.language}>"
