from fastapi import APIRouter

router = APIRouter()

from app.hello import routes  # noqa: E402,F401
