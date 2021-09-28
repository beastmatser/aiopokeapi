from ...minimal_resources import MinimalLanguage


class Description:
    description: str
    language: "MinimalLanguage"

    def __init__(self, data) -> None:
        self.description = data["description"]
        self.language = MinimalLanguage(data["language"])

    def __repr__(self) -> str:
        return f"<Description description='{self.description}' language={self.language}>"
