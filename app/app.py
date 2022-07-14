from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.routes.api import router
from app.core.config import get_app_settings
from app.core.events import create_start_app_handler, create_stop_app_handler
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
# from app.core.utils.middleware.brotli_middleware import BrotliMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from mangum import Mangum
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    settings = get_app_settings()

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    # application.add_middleware(BrotliMiddleware, minimum_size=100)
    application.add_middleware(GZipMiddleware, minimum_size=500)

    application.add_event_handler(
        'startup',
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        'shutdown',
        create_stop_app_handler(application),
    )
    application.include_router(
        router,
        prefix=settings.api_prefix
    )
    application.add_exception_handler(
        HTTPException,
        http_error_handler
    )
    application.add_exception_handler(
        RequestValidationError,
        http422_error_handler
    )
    return application


app = get_application()
# For AWS Lambda
handler = Mangum(app, lifespan='on')
