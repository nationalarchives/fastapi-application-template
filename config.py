import json
import os

from app.lib.util import strtobool


class Features(object):
    pass


class Base(object):
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "production")

    BUILD_VERSION: str = os.environ.get("BUILD_VERSION", "")

    SECRET_KEY: str = os.environ.get("SECRET_KEY", "")

    BASE_URI: str = os.environ.get("BASE_URI", "/api/v1")

    FORCE_HTTPS: bool = strtobool(os.getenv("FORCE_HTTPS", "True"))


class Production(Base, Features):
    pass


class Staging(Base, Features):
    pass


class Develop(Base, Features):
    FORCE_HTTPS = strtobool(os.getenv("FORCE_HTTPS", "False"))


class Test(Base, Features):
    ENVIRONMENT = "test"

    FORCE_HTTPS = False
