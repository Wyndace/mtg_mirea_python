from pydantic import BaseModel


class SubTypeSchema(BaseModel):
    id: int
    value: str

    class Config:
        from_attribute = True
