from typing import Optional

import aiofiles  # type: ignore

from aiopoke.objects.utility.common_models.sprite import Sprite

OptionalSprite = Optional["Sprite"]


class Sprites:
    back_default: OptionalSprite
    back_female: OptionalSprite
    back_shiny: OptionalSprite
    back_shiny_female: OptionalSprite
    front_default: OptionalSprite
    front_female: OptionalSprite
    front_shiny: OptionalSprite
    front_shiny_female: OptionalSprite
    generation_1: Optional["GenerationISprites"]
    generation_2: Optional["GenerationIISprites"]
    generation_3: Optional["GenerationIIISprites"]
    generation_4: Optional["GenerationIVSprites"]
    generation_5: Optional["GenerationVSprites"]
    generation_6: Optional["GenerationVISprites"]
    generation_7: Optional["GenerationVIISprites"]
    generation_8: Optional["GenerationVIIISprites"]

    def __init__(self, data) -> None:
        self.back_default = Sprite.from_url(data["back_default"])
        self.back_female = Sprite.from_url(data["back_female"])
        self.back_shiny = Sprite.from_url(data["back_shiny"])
        self.back_shiny_female = Sprite.from_url(data["back_shiny_female"])

        self.front_default = Sprite.from_url(data["front_default"])
        self.front_female = Sprite.from_url(data["front_female"])
        self.front_shiny = Sprite.from_url(data["front_shiny"])
        self.front_shiny_female = Sprite.from_url(data["front_shiny_female"])
        if data.get("versions") is not None:
            self.generation_i = self.generation_1 = GenerationISprites(
                data["versions"]["generation-i"]
            )
            self.generation_ii = self.generation_2 = GenerationIISprites(
                data["versions"]["generation-ii"]
            )
            self.generation_iii = self.generation_3 = GenerationIIISprites(
                data["versions"]["generation-iii"]
            )
            self.generation_iv = self.generation_4 = GenerationIVSprites(
                data["versions"]["generation-iv"]
            )
            self.generation_v = self.generation_5 = GenerationVSprites(
                data["versions"]["generation-v"]
            )
            self.generation_vi = self.generation_6 = GenerationVISprites(
                data["versions"]["generation-vi"]
            )
            self.generation_vii = self.generation_7 = GenerationVIISprites(
                data["versions"]["generation-vii"]
            )
            self.generation_viii = self.generation_8 = GenerationVIIISprites(
                data["versions"]["generation-viii"]
            )


class GenerationISprites:
    red_blue_back_default: OptionalSprite
    red_blue_back_gray: OptionalSprite
    red_blue_front_default: OptionalSprite
    red_blue_front_gray: OptionalSprite
    yellow_back_default: OptionalSprite
    yellow_back_gray: OptionalSprite
    yellow_front_default: OptionalSprite
    yellow_front_gray: OptionalSprite

    def __init__(self, data) -> None:
        self.red_blue_back_default = Sprite.from_url(data["red-blue"]["back_default"])
        self.red_blue_back_gray = Sprite.from_url(data["red-blue"]["back_gray"])
        self.red_blue_front_default = Sprite.from_url(data["red-blue"]["front_default"])
        self.red_blue_front_gray = Sprite.from_url(data["red-blue"]["front_gray"])

        self.yellow_back_default = Sprite.from_url(data["yellow"]["back_default"])
        self.yellow_back_gray = Sprite.from_url(data["yellow"]["back_gray"])
        self.yellow_front_default = Sprite.from_url(data["yellow"]["front_default"])
        self.yellow_front_gray = Sprite.from_url(data["yellow"]["front_gray"])


class GenerationIISprites:
    crystal_back_default: OptionalSprite
    crystal_back_shiny: OptionalSprite
    crystal_front_default: OptionalSprite
    crystal_front_shiny: OptionalSprite
    gold_back_default: OptionalSprite
    gold_back_shiny: OptionalSprite
    gold_front_default: OptionalSprite
    gold_front_shiny: OptionalSprite
    silver_back_default: OptionalSprite
    silver_back_shiny: OptionalSprite
    silver_front_default: OptionalSprite
    silver_front_shiny: OptionalSprite

    def __init__(self, data) -> None:
        self.crystal_back_default = Sprite.from_url(data["crystal"]["back_default"])
        self.crystal_back_shiny = Sprite.from_url(data["crystal"]["back_shiny"])
        self.crystal_front_default = Sprite.from_url(data["crystal"]["front_default"])
        self.crystal_front_shiny = Sprite.from_url(data["crystal"]["front_shiny"])

        self.gold_back_default = Sprite.from_url(data["gold"]["back_default"])
        self.gold_back_shiny = Sprite.from_url(data["gold"]["back_shiny"])
        self.gold_front_default = Sprite.from_url(data["gold"]["front_default"])
        self.gold_front_shiny = Sprite.from_url(data["gold"]["front_shiny"])

        self.silver_back_default = Sprite.from_url(data["silver"]["back_default"])
        self.silver_back_shiny = Sprite.from_url(data["silver"]["back_shiny"])
        self.silver_front_default = Sprite.from_url(data["silver"]["front_default"])
        self.silver_front_shiny = Sprite.from_url(data["silver"]["front_shiny"])


class GenerationIIISprites:
    emerald_front_default: OptionalSprite
    emerald_front_shiny: OptionalSprite
    firered_leafgreen_back_default: OptionalSprite
    firered_leafgreen_back_shiny: OptionalSprite
    firered_leafgreen_front_default: OptionalSprite
    firered_leafgreen_front_gray: OptionalSprite
    ruby_sapphire_back_default: OptionalSprite
    ruby_sapphire_back_shiny: OptionalSprite
    ruby_sapphire_front_default: OptionalSprite
    ruby_sapphire_front_shiny: OptionalSprite

    def __init__(self, data) -> None:
        self.emerald_front_default = Sprite.from_url(data["emerald"]["front_default"])
        self.emerald_front_shiny = Sprite.from_url(data["emerald"]["front_shiny"])

        self.firered_leafgreen_back_default = Sprite.from_url(
            data["firered-leafgreen"]["back_default"]
        )
        self.firered_leafgreen_back_shiny = Sprite.from_url(
            data["firered-leafgreen"]["back_shiny"]
        )
        self.firered_leafgreen_front_default = Sprite.from_url(
            data["firered-leafgreen"]["front_default"]
        )
        self.firered_leafgreen_front_shiny = Sprite.from_url(
            data["firered-leafgreen"]["front_shiny"]
        )

        self.ruby_sapphire_back_default = Sprite.from_url(
            data["ruby-sapphire"]["back_default"]
        )
        self.ruby_sapphire_back_shiny = Sprite.from_url(
            data["ruby-sapphire"]["back_shiny"]
        )
        self.ruby_sapphire_front_default = Sprite.from_url(
            data["ruby-sapphire"]["front_default"]
        )
        self.ruby_sapphire_front_shiny = Sprite.from_url(
            data["ruby-sapphire"]["front_shiny"]
        )


class GenerationIVSprites:
    diamond_pearl_back_default: OptionalSprite
    diamond_pearl_back_female: OptionalSprite
    diamond_pearl_back_shiny: OptionalSprite
    diamond_pearl_back_shiny_female: OptionalSprite
    diamond_pearl_front_default: OptionalSprite
    diamond_pearl_front_female: OptionalSprite
    diamond_pearl_front_shiny: OptionalSprite
    diamond_pearl_front_shiny_female: OptionalSprite
    heartgold_soulsilver_back_default: OptionalSprite
    heartgold_soulsilver_back_female: OptionalSprite
    heartgold_soulsilver_back_shiny: OptionalSprite
    heartgold_soulsilver_back_shiny_female: OptionalSprite
    heartgold_soulsilver_front_default: OptionalSprite
    heartgold_soulsilver_front_female: OptionalSprite
    heartgold_soulsilver_front_shiny: OptionalSprite
    heartgold_soulsilver_front_shiny_female: OptionalSprite
    platinum_back_default: OptionalSprite
    platinum_back_female: OptionalSprite
    platinum_back_shiny: OptionalSprite
    platinum_back_shiny_female: OptionalSprite
    platinum_front_default: OptionalSprite
    platinum_front_female: OptionalSprite
    platinum_front_shiny: OptionalSprite
    platinum_front_shiny_female: OptionalSprite

    def __init__(self, data) -> None:
        self.diamond_pearl_back_default = Sprite.from_url(
            data["diamond-pearl"]["back_default"]
        )
        self.diamond_pearl_back_female = Sprite.from_url(
            data["diamond-pearl"]["back_female"]
        )
        self.diamond_pearl_back_shiny = Sprite.from_url(
            data["diamond-pearl"]["back_shiny"]
        )
        self.diamond_pearl_back_shiny_female = Sprite.from_url(
            data["diamond-pearl"]["back_shiny_female"]
        )
        self.diamond_pearl_front_default = Sprite.from_url(
            data["diamond-pearl"]["front_default"]
        )
        self.diamond_pearl_front_female = Sprite.from_url(
            data["diamond-pearl"]["front_female"]
        )
        self.diamond_pearl_front_shiny = Sprite.from_url(
            data["diamond-pearl"]["front_shiny"]
        )
        self.diamond_pearl_front_shiny_female = Sprite.from_url(
            data["diamond-pearl"]["front_shiny_female"]
        )

        self.heartgold_soulsilver_back_default = Sprite.from_url(
            data["heartgold-soulsilver"]["back_default"]
        )
        self.heartgold_soulsilver_back_female = Sprite.from_url(
            data["heartgold-soulsilver"]["back_female"]
        )
        self.heartgold_soulsilver_back_shiny = Sprite.from_url(
            data["heartgold-soulsilver"]["back_shiny"]
        )
        self.heartgold_soulsilver_back_shiny_female = Sprite.from_url(
            data["heartgold-soulsilver"]["back_shiny_female"]
        )
        self.heartgold_soulsilver_front_default = Sprite.from_url(
            data["heartgold-soulsilver"]["front_default"]
        )
        self.heartgold_soulsilver_front_female = Sprite.from_url(
            data["heartgold-soulsilver"]["front_female"]
        )
        self.heartgold_soulsilver_front_shiny = Sprite.from_url(
            data["heartgold-soulsilver"]["front_shiny"]
        )
        self.heartgold_soulsilver_front_shiny_female = Sprite.from_url(
            data["heartgold-soulsilver"]["front_shiny_female"]
        )

        self.platinum_back_default = Sprite.from_url(data["platinum"]["back_default"])
        self.platinum_back_female = Sprite.from_url(data["platinum"]["back_female"])
        self.platinum_back_shiny = Sprite.from_url(data["platinum"]["back_shiny"])
        self.platinum_back_shiny_female = Sprite.from_url(
            data["platinum"]["back_shiny_female"]
        )
        self.platinum_front_default = Sprite.from_url(data["platinum"]["front_default"])
        self.platinum_front_female = Sprite.from_url(data["platinum"]["front_female"])
        self.platinum_front_shiny = Sprite.from_url(data["platinum"]["front_shiny"])
        self.platinum_front_shiny_female = Sprite.from_url(
            data["platinum"]["front_shiny_female"]
        )


class GenerationVSprites:
    black_white_animated_back_default: OptionalSprite
    black_white_animated_back_female: OptionalSprite
    black_white_animated_back_shiny: OptionalSprite
    black_white_animated_back_shiny_female: OptionalSprite
    black_white_animated_front_default: OptionalSprite
    black_white_animated_front_female: OptionalSprite
    black_white_animated_front_shiny: OptionalSprite
    black_white_animated_front_shiny_female: OptionalSprite
    black_white_back_default: OptionalSprite
    black_white_back_female: OptionalSprite
    black_white_back_shiny: OptionalSprite
    black_white_back_shiny_female: OptionalSprite
    black_white_front_default: OptionalSprite
    black_white_front_female: OptionalSprite
    black_white_front_shiny: OptionalSprite
    black_white_front_shiny_female: OptionalSprite

    def __init__(self, data) -> None:
        self.black_white_animated_back_default = Sprite.from_url(
            data["black-white"]["animated"]["back_default"]
        )
        self.black_white_animated_back_female = Sprite.from_url(
            data["black-white"]["animated"]["back_female"]
        )
        self.black_white_animated_back_shiny = Sprite.from_url(
            data["black-white"]["animated"]["back_shiny"]
        )
        self.black_white_animated_back_shiny_female = Sprite.from_url(
            data["black-white"]["animated"]["back_shiny_female"]
        )
        self.black_white_animated_front_default = Sprite.from_url(
            data["black-white"]["animated"]["front_default"]
        )
        self.black_white_animated_front_female = Sprite.from_url(
            data["black-white"]["animated"]["front_female"]
        )
        self.black_white_animated_front_shiny = Sprite.from_url(
            data["black-white"]["animated"]["front_shiny"]
        )
        self.black_white_animated_front_shiny_female = Sprite.from_url(
            data["black-white"]["animated"]["back_default"]
        )

        self.black_white_back_default = Sprite.from_url(
            data["black-white"]["back_default"]
        )
        self.black_white_back_female = Sprite.from_url(
            data["black-white"]["back_female"]
        )
        self.black_white_back_shiny = Sprite.from_url(data["black-white"]["back_shiny"])
        self.black_white_back_shiny_female = Sprite.from_url(
            data["black-white"]["back_shiny_female"]
        )
        self.black_white_front_default = Sprite.from_url(
            data["black-white"]["front_default"]
        )
        self.black_white_front_female = Sprite.from_url(
            data["black-white"]["front_female"]
        )
        self.black_white_front_shiny = Sprite.from_url(
            data["black-white"]["front_shiny"]
        )
        self.black_white_front_shiny_female = Sprite.from_url(
            data["black-white"]["back_default"]
        )


class GenerationVISprites:
    omegaruby_alphasapphire_front_default: OptionalSprite
    omegaruby_alphasapphire_front_female: OptionalSprite
    omegaruby_alphasapphire_front_shiny: OptionalSprite
    omegaruby_alphasapphire_front_shiny_female: OptionalSprite
    x_y_front_default: OptionalSprite
    x_y_front_female: OptionalSprite
    x_y_front_shiny: OptionalSprite
    x_y_front_shiny_female: OptionalSprite

    def __init__(self, data) -> None:
        self.omegaruby_alphasapphire_front_default = Sprite.from_url(
            data["omegaruby-alphasapphire"]["front_default"]
        )
        self.omegaruby_alphasapphire_front_female = Sprite.from_url(
            data["omegaruby-alphasapphire"]["front_female"]
        )
        self.omegaruby_alphasapphire_front_shiny = Sprite.from_url(
            data["omegaruby-alphasapphire"]["front_shiny"]
        )
        self.omegaruby_alphasapphire_front_shiny_female = Sprite.from_url(
            data["omegaruby-alphasapphire"]["front_shiny_female"]
        )

        self.x_y_front_default = Sprite.from_url(data["x-y"]["front_default"])
        self.x_y_front_female = Sprite.from_url(data["x-y"]["front_female"])
        self.x_y_front_shiny = Sprite.from_url(data["x-y"]["front_default"])
        self.x_y_front_shiny_female = Sprite.from_url(data["x-y"]["front_shiny_female"])


class GenerationVIISprites:
    icons_front_default: OptionalSprite
    icons_front_female: OptionalSprite
    ultra_sun_ultra_moon_front_default: OptionalSprite
    ultra_sun_ultra_moon_front_female: OptionalSprite
    ultra_sun_ultra_moon_front_shiny: OptionalSprite
    ultra_sun_ultra_moon_front_shiny_female: OptionalSprite

    def __init__(self, data) -> None:
        self.icons_front_default = Sprite.from_url(data["icons"]["front_default"])
        self.icons_front_female = Sprite.from_url(data["icons"]["front_female"])

        self.ultra_sun_ultra_moon_front_default = Sprite.from_url(
            data["ultra-sun-ultra-moon"]["front_default"]
        )
        self.ultra_sun_ultra_moon_front_female = Sprite.from_url(
            data["ultra-sun-ultra-moon"]["front_female"]
        )
        self.ultra_sun_ultra_moon_front_shiny = Sprite.from_url(
            data["ultra-sun-ultra-moon"]["front_default"]
        )
        self.ultra_sun_ultra_moon_front_shiny_female = Sprite.from_url(
            data["ultra-sun-ultra-moon"]["front_shiny_female"]
        )


class GenerationVIIISprites:
    icons_front_default: OptionalSprite
    icons_front_female: OptionalSprite

    def __init__(self, data) -> None:
        self.icons_front_default = Sprite.from_url(data["icons"]["front_default"])
        self.icons_front_female = Sprite.from_url(data["icons"]["front_female"])
