from app.hello import router
from pydantic import BaseModel


class GreetingResponse(BaseModel):
    message: str

    def __init__(self, greeting: str, name: str):
        super().__init__(message=f"{greeting}, {name}")


@router.get("/")
async def hello(
    name: str = "stranger",
) -> GreetingResponse:
    response = GreetingResponse(greeting="Hello", name=name)
    return response
