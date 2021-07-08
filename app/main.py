from fastapi import FastAPI, HTTPException
# from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
# from app.api.api_v1.errors.http_error import http_error_handler
# from app.api.api_v1.errors.validation_error import validation_exception_handler
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

# Add exceptions handler if you wanna.
# application.add_exception_handler(HTTPException, http_error_handler)
# application.add_exception_handler(RequestValidationError, validation_exception_handler)
