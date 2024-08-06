from app.greetings import router
from pydantic import BaseModel


class GreetingResponse(BaseModel):
    message: str

    def __init__(self, greeting: str, name: str):
        super().__init__(message=f"{greeting}, {name}")


@router.get("/hello/")
async def hello(
    name: str,
) -> GreetingResponse:
    response = GreetingResponse(greeting="Hello", name=name)
    return response


@router.get("/{greeting}/")
async def greeting(
    greeting: str,
    name: str,
) -> GreetingResponse:
    response = GreetingResponse(greeting=greeting, name=name)
    return response
