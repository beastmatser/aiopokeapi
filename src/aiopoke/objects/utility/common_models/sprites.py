from typing import Optional

from aiopoke.objects.utility.common_models.sprite import Sprite


class Sprites:
    back_default: Optional["Sprite"]
    back_female: Optional["Sprite"]
    back_shiny: Optional["Sprite"]
    back_shiny_female: Optional["Sprite"]
    front_default: Optional["Sprite"]
    front_female: Optional["Sprite"]
    front_shiny: Optional["Sprite"]
    front_shiny_female: Optional["Sprite"]
    generation_1: Optional["GenerationISprites"]
    generation_2: Optional["GenerationIISprites"]
    generation_3: Optional["GenerationIIISprites"]
    generation_4: Optional["GenerationIVSprites"]
    generation_5: Optional["GenerationVSprites"]
    generation_6: Optional["GenerationVISprites"]
    generation_7: Optional["GenerationVIISprites"]
    generation_8: Optional["GenerationVIIISprites"]
    other: Optional["Other"]

    def __init__(self, data) -> None:
        self.back_default = Sprite(data.get("back_default"))
        self.back_female = Sprite(data.get("back_female"))
        self.back_shiny = Sprite(data.get("back_shiny"))
        self.back_shiny_female = Sprite(data.get("back_shiny_female"))

        self.front_default = Sprite(data.get("front_default"))
        self.front_female = Sprite(data.get("front_female"))
        self.front_shiny = Sprite(data.get("front_shiny"))
        self.front_shiny_female = Sprite(data.get("front_shiny_female"))
        versions = data.get("versions")
        if versions is not None:
            self.generation_i = self.generation_1 = (
                GenerationISprites(versions["generation-i"])
                if "generation-i" in versions
                else None
            )
            self.generation_ii = self.generation_2 = (
                GenerationIISprites(versions["generation-ii"])
                if "generation-ii" in versions
                else None
            )
            self.generation_iii = self.generation_3 = (
                GenerationIIISprites(versions["generation-iii"])
                if "generation-iii" in versions
                else None
            )
            self.generation_iv = self.generation_4 = (
                GenerationIVSprites(versions["generation-iv"])
                if "generation-iv" in versions
                else None
            )
            self.generation_v = self.generation_5 = (
                GenerationVSprites(versions["generation-v"])
                if "generation-v" in versions
                else None
            )
            self.generation_vi = self.generation_6 = (
                GenerationVISprites(versions["generation-vi"])
                if "generation-vi" in versions
                else None
            )
            self.generation_vii = self.generation_7 = (
                GenerationVIISprites(versions["generation-vii"])
                if "generation-vii" in versions
                else None
            )
            self.generation_viii = self.generation_8 = (
                GenerationVIIISprites(versions["generation-viii"])
                if "generation-viii" in versions
                else None
            )
        self.other = Other(data["other"]) if data.get("other") is not None else None


class GenerationISprites:
    red_blue_back_default: Optional["Sprite"]
    red_blue_back_gray: Optional["Sprite"]
    red_blue_front_default: Optional["Sprite"]
    red_blue_front_gray: Optional["Sprite"]
    yellow_back_default: Optional["Sprite"]
    yellow_back_gray: Optional["Sprite"]
    yellow_front_default: Optional["Sprite"]
    yellow_front_gray: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.red_blue_back_default = Sprite(data["red-blue"]["back_default"])
        self.red_blue_back_gray = Sprite(data["red-blue"]["back_gray"])
        self.red_blue_front_default = Sprite(data["red-blue"]["front_default"])
        self.red_blue_front_gray = Sprite(data["red-blue"]["front_gray"])

        self.yellow_back_default = Sprite(data["yellow"]["back_default"])
        self.yellow_back_gray = Sprite(data["yellow"]["back_gray"])
        self.yellow_front_default = Sprite(data["yellow"]["front_default"])
        self.yellow_front_gray = Sprite(data["yellow"]["front_gray"])


class GenerationIISprites:
    crystal_back_default: Optional["Sprite"]
    crystal_back_shiny: Optional["Sprite"]
    crystal_front_default: Optional["Sprite"]
    crystal_front_shiny: Optional["Sprite"]
    gold_back_default: Optional["Sprite"]
    gold_back_shiny: Optional["Sprite"]
    gold_front_default: Optional["Sprite"]
    gold_front_shiny: Optional["Sprite"]
    silver_back_default: Optional["Sprite"]
    silver_back_shiny: Optional["Sprite"]
    silver_front_default: Optional["Sprite"]
    silver_front_shiny: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.crystal_back_default = Sprite(data["crystal"]["back_default"])
        self.crystal_back_shiny = Sprite(data["crystal"]["back_shiny"])
        self.crystal_front_default = Sprite(data["crystal"]["front_default"])
        self.crystal_front_shiny = Sprite(data["crystal"]["front_shiny"])

        self.gold_back_default = Sprite(data["gold"]["back_default"])
        self.gold_back_shiny = Sprite(data["gold"]["back_shiny"])
        self.gold_front_default = Sprite(data["gold"]["front_default"])
        self.gold_front_shiny = Sprite(data["gold"]["front_shiny"])

        self.silver_back_default = Sprite(data["silver"]["back_default"])
        self.silver_back_shiny = Sprite(data["silver"]["back_shiny"])
        self.silver_front_default = Sprite(data["silver"]["front_default"])
        self.silver_front_shiny = Sprite(data["silver"]["front_shiny"])


class GenerationIIISprites:
    emerald_front_default: Optional["Sprite"]
    emerald_front_shiny: Optional["Sprite"]
    firered_leafgreen_back_default: Optional["Sprite"]
    firered_leafgreen_back_shiny: Optional["Sprite"]
    firered_leafgreen_front_default: Optional["Sprite"]
    firered_leafgreen_front_gray: Optional["Sprite"]
    ruby_sapphire_back_default: Optional["Sprite"]
    ruby_sapphire_back_shiny: Optional["Sprite"]
    ruby_sapphire_front_default: Optional["Sprite"]
    ruby_sapphire_front_shiny: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.emerald_front_default = Sprite(data["emerald"]["front_default"])
        self.emerald_front_shiny = Sprite(data["emerald"]["front_shiny"])

        self.firered_leafgreen_back_default = Sprite(
            data["firered-leafgreen"]["back_default"]
        )
        self.firered_leafgreen_back_shiny = Sprite(
            data["firered-leafgreen"]["back_shiny"]
        )
        self.firered_leafgreen_front_default = Sprite(
            data["firered-leafgreen"]["front_default"]
        )
        self.firered_leafgreen_front_shiny = Sprite(
            data["firered-leafgreen"]["front_shiny"]
        )

        self.ruby_sapphire_back_default = Sprite(data["ruby-sapphire"]["back_default"])
        self.ruby_sapphire_back_shiny = Sprite(data["ruby-sapphire"]["back_shiny"])
        self.ruby_sapphire_front_default = Sprite(
            data["ruby-sapphire"]["front_default"]
        )
        self.ruby_sapphire_front_shiny = Sprite(data["ruby-sapphire"]["front_shiny"])


class GenerationIVSprites:
    diamond_pearl_back_default: Optional["Sprite"]
    diamond_pearl_back_female: Optional["Sprite"]
    diamond_pearl_back_shiny: Optional["Sprite"]
    diamond_pearl_back_shiny_female: Optional["Sprite"]
    diamond_pearl_front_default: Optional["Sprite"]
    diamond_pearl_front_female: Optional["Sprite"]
    diamond_pearl_front_shiny: Optional["Sprite"]
    diamond_pearl_front_shiny_female: Optional["Sprite"]
    heartgold_soulsilver_back_default: Optional["Sprite"]
    heartgold_soulsilver_back_female: Optional["Sprite"]
    heartgold_soulsilver_back_shiny: Optional["Sprite"]
    heartgold_soulsilver_back_shiny_female: Optional["Sprite"]
    heartgold_soulsilver_front_default: Optional["Sprite"]
    heartgold_soulsilver_front_female: Optional["Sprite"]
    heartgold_soulsilver_front_shiny: Optional["Sprite"]
    heartgold_soulsilver_front_shiny_female: Optional["Sprite"]
    platinum_back_default: Optional["Sprite"]
    platinum_back_female: Optional["Sprite"]
    platinum_back_shiny: Optional["Sprite"]
    platinum_back_shiny_female: Optional["Sprite"]
    platinum_front_default: Optional["Sprite"]
    platinum_front_female: Optional["Sprite"]
    platinum_front_shiny: Optional["Sprite"]
    platinum_front_shiny_female: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.diamond_pearl_back_default = Sprite(data["diamond-pearl"]["back_default"])
        self.diamond_pearl_back_female = Sprite(data["diamond-pearl"]["back_female"])
        self.diamond_pearl_back_shiny = Sprite(data["diamond-pearl"]["back_shiny"])
        self.diamond_pearl_back_shiny_female = Sprite(
            data["diamond-pearl"]["back_shiny_female"]
        )
        self.diamond_pearl_front_default = Sprite(
            data["diamond-pearl"]["front_default"]
        )
        self.diamond_pearl_front_female = Sprite(data["diamond-pearl"]["front_female"])
        self.diamond_pearl_front_shiny = Sprite(data["diamond-pearl"]["front_shiny"])
        self.diamond_pearl_front_shiny_female = Sprite(
            data["diamond-pearl"]["front_shiny_female"]
        )

        self.heartgold_soulsilver_back_default = Sprite(
            data["heartgold-soulsilver"]["back_default"]
        )
        self.heartgold_soulsilver_back_female = Sprite(
            data["heartgold-soulsilver"]["back_female"]
        )
        self.heartgold_soulsilver_back_shiny = Sprite(
            data["heartgold-soulsilver"]["back_shiny"]
        )
        self.heartgold_soulsilver_back_shiny_female = Sprite(
            data["heartgold-soulsilver"]["back_shiny_female"]
        )
        self.heartgold_soulsilver_front_default = Sprite(
            data["heartgold-soulsilver"]["front_default"]
        )
        self.heartgold_soulsilver_front_female = Sprite(
            data["heartgold-soulsilver"]["front_female"]
        )
        self.heartgold_soulsilver_front_shiny = Sprite(
            data["heartgold-soulsilver"]["front_shiny"]
        )
        self.heartgold_soulsilver_front_shiny_female = Sprite(
            data["heartgold-soulsilver"]["front_shiny_female"]
        )

        self.platinum_back_default = Sprite(data["platinum"]["back_default"])
        self.platinum_back_female = Sprite(data["platinum"]["back_female"])
        self.platinum_back_shiny = Sprite(data["platinum"]["back_shiny"])
        self.platinum_back_shiny_female = Sprite(data["platinum"]["back_shiny_female"])
        self.platinum_front_default = Sprite(data["platinum"]["front_default"])
        self.platinum_front_female = Sprite(data["platinum"]["front_female"])
        self.platinum_front_shiny = Sprite(data["platinum"]["front_shiny"])
        self.platinum_front_shiny_female = Sprite(
            data["platinum"]["front_shiny_female"]
        )


class GenerationVSprites:
    black_white_animated_back_default: Optional["Sprite"]
    black_white_animated_back_female: Optional["Sprite"]
    black_white_animated_back_shiny: Optional["Sprite"]
    black_white_animated_back_shiny_female: Optional["Sprite"]
    black_white_animated_front_default: Optional["Sprite"]
    black_white_animated_front_female: Optional["Sprite"]
    black_white_animated_front_shiny: Optional["Sprite"]
    black_white_animated_front_shiny_female: Optional["Sprite"]
    black_white_back_default: Optional["Sprite"]
    black_white_back_female: Optional["Sprite"]
    black_white_back_shiny: Optional["Sprite"]
    black_white_back_shiny_female: Optional["Sprite"]
    black_white_front_default: Optional["Sprite"]
    black_white_front_female: Optional["Sprite"]
    black_white_front_shiny: Optional["Sprite"]
    black_white_front_shiny_female: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.black_white_animated_back_default = Sprite(
            data["black-white"]["animated"]["back_default"]
        )
        self.black_white_animated_back_female = Sprite(
            data["black-white"]["animated"]["back_female"]
        )
        self.black_white_animated_back_shiny = Sprite(
            data["black-white"]["animated"]["back_shiny"]
        )
        self.black_white_animated_back_shiny_female = Sprite(
            data["black-white"]["animated"]["back_shiny_female"]
        )
        self.black_white_animated_front_default = Sprite(
            data["black-white"]["animated"]["front_default"]
        )
        self.black_white_animated_front_female = Sprite(
            data["black-white"]["animated"]["front_female"]
        )
        self.black_white_animated_front_shiny = Sprite(
            data["black-white"]["animated"]["front_shiny"]
        )
        self.black_white_animated_front_shiny_female = Sprite(
            data["black-white"]["animated"]["back_default"]
        )

        self.black_white_back_default = Sprite(data["black-white"]["back_default"])
        self.black_white_back_female = Sprite(data["black-white"]["back_female"])
        self.black_white_back_shiny = Sprite(data["black-white"]["back_shiny"])
        self.black_white_back_shiny_female = Sprite(
            data["black-white"]["back_shiny_female"]
        )
        self.black_white_front_default = Sprite(data["black-white"]["front_default"])
        self.black_white_front_female = Sprite(data["black-white"]["front_female"])
        self.black_white_front_shiny = Sprite(data["black-white"]["front_shiny"])
        self.black_white_front_shiny_female = Sprite(
            data["black-white"]["back_default"]
        )


class GenerationVISprites:
    omegaruby_alphasapphire_front_default: Optional["Sprite"]
    omegaruby_alphasapphire_front_female: Optional["Sprite"]
    omegaruby_alphasapphire_front_shiny: Optional["Sprite"]
    omegaruby_alphasapphire_front_shiny_female: Optional["Sprite"]
    x_y_front_default: Optional["Sprite"]
    x_y_front_female: Optional["Sprite"]
    x_y_front_shiny: Optional["Sprite"]
    x_y_front_shiny_female: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.omegaruby_alphasapphire_front_default = Sprite(
            data["omegaruby-alphasapphire"]["front_default"]
        )
        self.omegaruby_alphasapphire_front_female = Sprite(
            data["omegaruby-alphasapphire"]["front_female"]
        )
        self.omegaruby_alphasapphire_front_shiny = Sprite(
            data["omegaruby-alphasapphire"]["front_shiny"]
        )
        self.omegaruby_alphasapphire_front_shiny_female = Sprite(
            data["omegaruby-alphasapphire"]["front_shiny_female"]
        )

        self.x_y_front_default = Sprite(data["x-y"]["front_default"])
        self.x_y_front_female = Sprite(data["x-y"]["front_female"])
        self.x_y_front_shiny = Sprite(data["x-y"]["front_default"])
        self.x_y_front_shiny_female = Sprite(data["x-y"]["front_shiny_female"])


class GenerationVIISprites:
    icons_front_default: Optional["Sprite"]
    icons_front_female: Optional["Sprite"]
    ultra_sun_ultra_moon_front_default: Optional["Sprite"]
    ultra_sun_ultra_moon_front_female: Optional["Sprite"]
    ultra_sun_ultra_moon_front_shiny: Optional["Sprite"]
    ultra_sun_ultra_moon_front_shiny_female: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.icons_front_default = Sprite(data["icons"]["front_default"])
        self.icons_front_female = Sprite(data["icons"]["front_female"])

        self.ultra_sun_ultra_moon_front_default = Sprite(
            data["ultra-sun-ultra-moon"]["front_default"]
        )
        self.ultra_sun_ultra_moon_front_female = Sprite(
            data["ultra-sun-ultra-moon"]["front_female"]
        )
        self.ultra_sun_ultra_moon_front_shiny = Sprite(
            data["ultra-sun-ultra-moon"]["front_default"]
        )
        self.ultra_sun_ultra_moon_front_shiny_female = Sprite(
            data["ultra-sun-ultra-moon"]["front_shiny_female"]
        )


class GenerationVIIISprites:
    icons_front_default: Optional["Sprite"]
    icons_front_female: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.icons_front_default = Sprite(
            data["brilliant-diamond-shining-pearl"]["front_default"]
        )
        self.icons_front_female = Sprite(
            data["brilliant-diamond-shining-pearl"]["front_female"]
        )


class Other:
    dream_world_front_default: Optional["Sprite"]
    dream_world_front_female: Optional["Sprite"]
    home_front_default: Optional["Sprite"]
    home_front_female: Optional["Sprite"]
    home_front_shiny: Optional["Sprite"]
    home_front_shiny_female: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.dream_world_front_default = Sprite(data["dream_world"]["front_default"])
        self.dream_world_front_female = Sprite(data["dream_world"]["front_female"])
        self.home_front_default = Sprite(data["home"]["front_default"])
        self.home_front_female = Sprite(data["home"]["front_female"])
        self.home_front_shiny = Sprite(data["home"]["front_shiny"])
        self.home_front_shiny_female = Sprite(data["home"]["front_shiny_female"])
        self.official_artwork_front_default = Sprite(
            data["official-artwork"]["front_default"]
        )
        self.official_artwork_front_shiny = Sprite(
            data["official-artwork"]["front_shiny"]
        )
