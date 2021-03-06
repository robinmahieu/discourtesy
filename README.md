# Discourtesy

Discourtesy is a minimal framework to handle Discord interactions.

## Installation

Discourtesy requires [Python 3.10][python-3.10] or higher.

This package is available on PyPI, so use `pip` or another dependency manager to install it.

```sh
pip install discourtesy
```

## Introduction

A basic application with a simple beep boop command looks like this.

```py
import discourtesy

app = discourtesy.Application(application_id=0, public_key="", token="")


@discourtesy.command("beep")
async def beep_command(application, interaction):
    return "boop"


app.add_plugin(__name__)
```

First, the Discourtesy package is being imported and an application is being instantiated. Here, the application's ID, public key and token are set. This information can be found in [Discord's developer portal][discord-developer-portal].

Finally, the `beep` command is created. The callback provides the application instance and the interaction data, but neither is being used here. The file is being added as a plugin, which makes sure that the command is being registered properly.

To start the web server, use an ASGI server implementation. By default, [`uvicorn`][uvicorn] is included as a dependency in this package.

```sh
uvicorn filename:app
```

## Contributing

Before contributing to Discourtesy, make sure to read through the [contribution guidelines][contribution-guidelines].

This project is licensed under the terms of the [MIT][mit-license] license.

[contribution-guidelines]: <https://github.com/robinmahieu/discourtesy/blob/stardust/CONTRIBUTING.md>
[discord-developer-portal]: <https://discord.com/developers/applications>
[mit-license]: <https://github.com/robinmahieu/discourtesy/blob/stardust/LICENSE>
[python-3.10]: <https://www.python.org/downloads/>
[uvicorn]: <https://www.uvicorn.org/>
