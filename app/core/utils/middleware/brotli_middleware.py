
from app.core.utils.middleware.brotli_responser import BrotliResponser
from starlette.datastructures import Headers
from starlette.types import ASGIApp, Receive, Scope, Send


class BrotliMiddleware:
    def __init__(self, app: ASGIApp, minimum_size=100):
        self.app = app
        self.minimum_size = minimum_size

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        """_summary_

        _extended_summary_

        Args:
            scope (Scope): _description_
            receive (Receive): _description_
            send (Send): _description_
        """
        # checking the type of the request
        if scope['type'] == 'http':
            # check if the Accept-Encoding sent by the client
            headers = Headers(scope=scope)
            if 'br' in headers.get('Accept-Encoding', ''):
                responder = BrotliResponser(self.app, self.minimum_size)
                await responder(scope, receive, send)
                return

        await self.app(scope, receive, send)
