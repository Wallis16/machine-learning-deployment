from pydantic import BaseModel

class UserRegistry(BaseModel):
    name: str | None = None
    age: int | None = None