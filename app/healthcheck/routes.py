from app.healthcheck import router


@router.get("/live/", include_in_schema=False)
async def healthcheck() -> str:
    return "ok"
