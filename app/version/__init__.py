from fastapi import APIRouter

router = APIRouter()

from app.version import routes  # noqa: E402,F401
