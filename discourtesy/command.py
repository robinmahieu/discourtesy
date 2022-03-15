from loguru import logger
from starlette.responses import JSONResponse

from discourtesy.utils import simple_message


class Command:
    def __init__(self, name, coroutine, ephemeral, followup, input_type):
        self.name = name
        self.coroutine = coroutine

        self.ephemeral = ephemeral
        self.followup = followup
        self.input_type = input_type

    async def __call__(self, application, interaction):
        if self.followup:
            response = {"type": 5}

            followup = Followup(self, application, interaction)

            return JSONResponse(response, background=followup, status_code=200)

        response = (
            await self.coroutine(application, interaction)
            or "This command is currently not available."
        )

        logger.info(f"Command {self.name} executed.")

        if isinstance(response, str):
            response = simple_message(response)

        if self.ephemeral:
            response["flags"] = 64

        response = {"type": 4, "data": response}

        return JSONResponse(response, status_code=200)


class Followup:
    def __init__(self, command, application, interaction):
        self.command = command

        self.application = application
        self.interaction = interaction

    async def __call__(self):
        response = (
            await self.command.coroutine(self.application, self.interaction)
            or "This command is currently not available."
        )

        logger.info(f"Command {self.command.name} followup executed.")

        if isinstance(response, str):
            response = simple_message(response)

        if self.command.ephemeral:
            response["flags"] = 64

        await self.application.http.create_followup_message(
            self.interaction["token"], response
        )


def command(name, ephemeral=False, followup=False, input_type=1):
    def decorator(coroutine):
        return Command(name, coroutine, ephemeral, followup, input_type)

    return decorator
