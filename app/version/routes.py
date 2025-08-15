from app.lib.get_config import get_config
from app.version import router


@router.get("/", include_in_schema=False)
async def version() -> dict:
    config = get_config()
    return {
        "containerImage": config.get("CONTAINER_IMAGE"),
        "buildVersion": config.get("BUILD_VERSION"),
    }
