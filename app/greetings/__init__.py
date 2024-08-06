from fastapi import APIRouter

router = APIRouter()

from app.greetings import routes  # noqa: E402,F401
