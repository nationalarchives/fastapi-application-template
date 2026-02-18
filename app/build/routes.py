from app.build import router
from app.lib.get_config import get_config


@router.get("/")
async def build() -> dict:
    config = get_config()
    return {
        "containerImage": config.get("CONTAINER_IMAGE"),
        "buildVersion": config.get("BUILD_VERSION"),
    }
