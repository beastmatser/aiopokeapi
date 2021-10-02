import aiopoke
import asyncio
import discord
import inspect
from discord.ext import commands

# create out bot wiht the poke_client
class Bot(commands.Bot):
    poke_client: aiopoke.AiopokeClient

    def __init__(self, poke_client):
        super().__init__(command_prefix="?")

        # this means that our poke_client object can be accessed trough self.bot.poke_client (in cogs)
        self.poke_client = poke_client

        # add our cog
        self.add_cog(PokemonCog(self))

    async def on_ready(self):
        print(f"{self.user} is ready!")


class PokemonCog(commands.Cog):
    bot: "Bot"

    def __init__(self, bot) -> None:
        self.bot = bot

    # a simple pokemon command
    @commands.command()
    async def pokemon(self, ctx: commands.Context, name_or_id):
        pokemon = await self.bot.poke_client.fetch_pokemon(name_or_id)
        if pokemon is None:
            return await ctx.send(f"This is not a valid pokemon name or id!")

        pokemon_species = await pokemon.species.fetch()

        # this is just a simple example it's up to you which data you want to include
        embed = discord.Embed(
            title=f"{pokemon.name.title()}",
            description=inspect.cleandoc(
                f"""
                ID: {pokemon.id_}
                Abilities: {', '.join([pokemon_ability.ability.name for pokemon_ability in pokemon.abilities])}
                Species: {pokemon_species.name} (ID: {pokemon_species.id_})
                    - Capture rate: {pokemon_species.capture_rate}
                    - Color: {pokemon_species.color.name}
                Height: {pokemon.height}
                Weight: {pokemon.weight}
                """
            )
            )
        embed.set_thumbnail(url=pokemon.sprites.front_default.url)
        await ctx.send(embed=embed)


async def main():
    async with aiopoke.AiopokeClient() as poke_client:
        bot = Bot(poke_client)
        await bot.start("TOKEN")


asyncio.run(main())
