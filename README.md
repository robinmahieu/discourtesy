# Discourtesy

Discourtesy is a minimal framework to handle Discord interactions.

## Installation

Discourtesy requires [Python 3.10][python-3.10] or higher.

The package is available on PyPi, so install it with `pip` or another dependency manager.

```bash
pip install discourtesy
```

## Introduction

A basic application with a simple beep boop command looks like this.

```py
import discourtesy

application = discourtesy.Application(application_id=0, public_key="", token="")


@discourtesy.command("beep")
async def beep_command(application, interaction):
    return "boop"


application.add_plugin(__name__)
```

First, the Discourtesy package is being imported and an application is being instantiated. Next, the application's public key is being set, which is being used to verify incoming requests.

Finally, the `beep` command is being created. The callback provides the application instance and the interaction data, but neither is being used here. The file is being added as a plugin, which makes sure that the command is being registered properly.

To start the web server, use an ASGI server implementation like `uvicorn`.

```bash
uvicorn filename:application
```

## Contributing

Before contributing to Discourtesy, make sure to read through the [contribution guidelines][contribution-guidelines].

This project is licensed under the terms of the [MIT][mit-license] license.

[contribution-guidelines]: <https://github.com/robinmahieu/discourtesy/blob/stardust/CONTRIBUTING.md>
[mit-license]: <https://github.com/robinmahieu/discourtesy/blob/stardust/LICENSE>
[python-3.10]: <https://www.python.org/downloads/>
