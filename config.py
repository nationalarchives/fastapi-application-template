import os

from pydantic import field_validator
from pydantic_settings import BaseSettings


class Features(BaseSettings):
    pass


class Production(Features):
    CONTAINER_IMAGE: str = ""
    BUILD_VERSION: str = ""

    SECRET_KEY: str = ""

    @field_validator("SECRET_KEY")
    @classmethod
    def validate_secret_key(cls, value: str) -> str:
        if not value:
            raise ValueError("SECRET_KEY must be set")
        return value

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "WARNING")

    FORCE_HTTPS: bool = os.getenv("FORCE_HTTPS", "True").lower() != "false"

    BASE_URI: str = "api"

    @field_validator("BASE_URI")
    @classmethod
    def strip_base_uri_slashes(cls, value: str) -> str:
        return value.strip("/")


class Test(Production):
    BUILD_VERSION: str = "test"

    LOG_LEVEL: str = "DEBUG"

    FORCE_HTTPS: bool = False
