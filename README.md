# Discourtesy

Discourtesy is a minimal framework to handle Discord interactions.

## Installation

Discourtesy requires [Python 3.9][python-3.9] or higher.

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
