# Discourtesy

Discourtesy is a minimal framework to handle Discord interactions.

## Installation

Discourtesy requires [Python 3.9][python-3.9] or higher.

The package is available on PyPi, so install it with `pip` or another dependency manager.

```bash
pip install discourtesy
```

## Introduction

```py
import discourtesy

application = discourtesy.Application()

public_key = ""
application.set_public_key(public_key)


@discourtesy.command("beep")
async def beep_command(client, interaction):
    return "boop"


application.add_plugin(__name__)
```

```bash
uvicorn filename:application
```

[python-3.9]: <https://www.python.org/downloads/>
