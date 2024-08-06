from fastapi import APIRouter

router = APIRouter()

from app.healthcheck import routes  # noqa: E402,F401
