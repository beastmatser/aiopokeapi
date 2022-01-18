import asyncio

import aiopoke


async def main():
    async with aiopoke.AiopokeClient() as client:
        berry = await client.fetch_berry(1)
        print(berry.flavors)


asyncio.run(main())
