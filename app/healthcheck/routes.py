from app.healthcheck import router


@router.get("/live/")
async def healthcheck() -> str:
    return "ok"
