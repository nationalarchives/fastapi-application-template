import os

from app.lib.util import strtobool


class Features:
    pass


class Production(Features):
    CONTAINER_IMAGE: str = os.environ.get("CONTAINER_IMAGE", "")
    BUILD_VERSION: str = os.environ.get("BUILD_VERSION", "")

    SECRET_KEY: str = os.environ.get("SECRET_KEY", "")

    BASE_URI: str = os.environ.get("BASE_URI", "/api/").strip("/")

    FORCE_HTTPS: bool = strtobool(os.getenv("FORCE_HTTPS", "True"))


class Staging(Production):
    pass


class Develop(Production):
    pass


class Test(Production):
    FORCE_HTTPS = False
