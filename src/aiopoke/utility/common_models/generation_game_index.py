from ...minimal_resources import MinimalGeneration


class GenerationGameIndex:
    game_index: int
    generation: "MinimalGeneration"

    def __init__(self, data) -> None:
        self.game_index = data["game_index"]
        self.generation = MinimalGeneration(data["generation"])

    def __repr__(self) -> str:
        return f"<GenerationGameIndex game_index='{self.game_index}' generation={self.generation}>"
