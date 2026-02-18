from app.healthcheck import router
from app.lib.get_config import get_config


@router.get("/live/")
async def healthcheck() -> str:
    return "ok"


@router.get("/version/")
async def healthcheck_version() -> str:
    config = get_config()
    return config.get("BUILD_VERSION", "")
