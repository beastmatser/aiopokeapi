from ...minimal_resources import MinimalLanguage


class Effect:
    effect: str
    language: "MinimalLanguage"

    def __init__(self, data) -> None:
        self.effect = data["effect"]
        self.language = MinimalLanguage(data["language"])

    def __repr__(self) -> str:
        return f"<Effect effect='{self.effect}' language={self.language}>"
