import datetime

from loguru import logger
from starlette.responses import JSONResponse

from discourtesy.utils import simple_message


class Component:
    def __init__(self, name, coroutine, callback_type, timeout):
        self.name = name
        self.coroutine = coroutine

        self.callback_type = callback_type
        self.timeout = timeout

    async def __call__(self, application, interaction):
        if self.timeout:
            start = datetime.datetime.fromisoformat(
                interaction["message"]["timestamp"]
            )
            now = datetime.datetime.now(datetime.timezone.utc)

            if int((now - start).total_seconds()) > self.timeout:
                logger.info(f"Component {self.name} failed, timed out.")

                return JSONResponse({"type": 6}, status_code=200)

        response = await self.coroutine(application, interaction)

        logger.info(f"Component {self.name} executed.")

        if isinstance(response, str):
            response = simple_message(response)

        if response:
            response = {"type": self.callback_type, "data": response}
        else:
            response = {"type": 6}

        return JSONResponse(response, status_code=200)


def component(name, callback_type=7, timeout=0):
    def decorator(coroutine):
        return Component(name, coroutine, callback_type, timeout)

    return decorator
