# Aiopokeapi

 An asynchronous API wrapper for the [pokeapi](https://pokeapi.co/) written in Python.

![Tests](https://github.com/beastmatser/aiopokeapi/actions/workflows/tests.yml/badge.svg)
![Pypi](https://img.shields.io/pypi/v/aiopokeapi.svg)
![Python](https://img.shields.io/pypi/pyversions/aiopokeapi.svg)

## Key Features

- Use of modern Python keywords: `async` and `await`.
- Fully typehinted, no need to look at documentations!
- Objects get cached, this increases speed and avoids unnecessary API requests.

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

asyncio.run(main())
```
