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

Aiopoke's goal is to be simple and easy to use:

```py
import asyncio
import aiopoke


async def main():
    client = aiopoke.AiopokeClient()

    ability = await client.get_ability(1)
    print(ability)

    await client.close()

asyncio.run(main())
```

Or even better, using a context manager:

```py
# in main()
async with aiopoke.AiopokeClient() as client:
    ability = await client.get_ability(1)
    print(ability)

```
