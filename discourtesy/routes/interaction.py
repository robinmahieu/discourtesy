from loguru import logger
from nacl.exceptions import BadSignatureError
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route


class InteractionRoute(Route):
    def __init__(self):
        super().__init__("/interaction", self.endpoint, methods=["POST"])

    async def endpoint(self, request):
        try:
            signature = request.headers["X-Signature-Ed25519"]
            timestamp = request.headers["X-Signature-Timestamp"]
        except KeyError:
            return PlainTextResponse("Bad Request", status_code=400)

        body = await request.body()

        try:
            request.app.verify_key.verify(
                timestamp.encode() + body, bytes.fromhex(signature)
            )
        except BadSignatureError:
            return PlainTextResponse("Unauthorized", status_code=401)

        response = PlainTextResponse("Bad Request", status_code=400)

        interaction = await request.json()

        match interaction["type"]:
            case 1:
                logger.debug("Received T1 PING.")
                response = JSONResponse({"type": 1}, status_code=200)

            case 2:
                logger.debug("Received T2 APPLICATION_COMMAND.")
                response = await request.app.dispatch.execute_command(
                    request.app, interaction
                )

            case 3:
                logger.debug("Received T3 MESSAGE_COMPONENT.")
                response = await request.app.dispatch.execute_component(
                    request.app, interaction
                )

        return response
