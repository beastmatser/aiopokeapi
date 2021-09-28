import asyncio
import aiopoke


async def main():
    async with aiopoke.AiopokeClient() as client:
        pokemon = await client.fetch_pokemon("pikachu")  # pokemon will be typehinted
        print(pokemon)

# this will most likely raise
# Exception ignored in: <function _ProactorBasePipeTransport.__del__ at 0x000001DF496B0040>
# this is a bug with asyncio to ignore this you can add
# asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
asyncio.run(main())
