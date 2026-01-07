from fastapi import APIRouter

router = APIRouter()

from app.build import routes  # noqa: E402,F401
