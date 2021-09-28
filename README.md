# Aiopokeapi

 An asynchronous API wrapper for pokeapi written in Python. Not only is this package asynchronous, it is also fully typed, meaning you don't have to look back and forth at documentations.

![Tests](https://github.com/beastmatser/aiopokeapi/actions/workflows/tests.yml/badge.svg)

## Installation

```sh
pip install aiopokeapi
```

## Getting started

```py
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
```
