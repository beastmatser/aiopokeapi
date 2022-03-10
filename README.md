<p align="center">
   <img src="assets/aiopokeapi-readme-banner.png">
   <h1 align="center"> AioPokéApi</h1>
   <p align="center"> An Asynchronous API wrapper for the <a href="https://pokeapi.co">PokéApi</a> written in <b>Python</b>.
</p>
<p align="center">
   <img id="tests" src="https://img.shields.io/github/workflow/status/beastmatser/aiopokeapi/tests?label=Tests&logo=github&style=flat-square">
   <img id="pypi-version" src="https://img.shields.io/pypi/v/aiopokeapi?label=Pypi%20version&logo=pypi&logoColor=ffffff&style=flat-square">
   <img id="python-version" src="https://img.shields.io/pypi/pyversions/aiopokeapi?label=Python%20version&logo=python&logoColor=ffffff&style=flat-square">
   <img id="license" src="https://img.shields.io/github/license/beastmatser/aiopokeapi?label=License&style=flat-square">
   <img id="style" src="https://img.shields.io/badge/Code%20style-black-black?style=flat-square">
</p>
<p align="center">
   <a href="https://github.com/beastmatser/aiopokeapi/issues/new/choose"> Report issue</a>
   ·
   <a href="https://github.com/beastmatser/aiopokeapi/issues/new/choose"> Request feature</a>
   ·
   <a href="https://github.com/beastmatser/aiopokeapi/fork"> Fork project</a>
</p>

## :old_key: Key Features

- Use of modern Python keywords: `async` and `await`.
- Every object is fully type hinted.
- Objects get cached, this increases speed and avoids unnecessary API requests.

## :earth_africa: Documentation

AioPokéApi has a very minimal website, which you can find [here](https://beastmatser.github.io/aiopoke/). It also has some [documentation](https://beastmatser.github.io/aiopoke/docs/).

## :comet: Installation

```sh
pip install aiopokeapi
```

<details>

<summary>
    :gear: <i> Didn't work?</i>
</summary>

Depending on your Python installation, you might need to use one of the
following:

- Python is not in PATH

  ```sh
  path/to/python.exe -m pip install aiopokeapi
  ```

- Python is in PATH but pip is not

  ```sh
  python -m pip install aiopokeapi
  ```

- Unix systems can use pip3/python3 commands

  ```sh
  pip3 install aiopokeapi
  ```

  ```sh
  python3 -m pip install aiopokeapi
  ```

- Using multiple Python versions

  ```sh
  py -m pip install aiopokeapi
  ```

</details>

## :rocket: Getting started

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
