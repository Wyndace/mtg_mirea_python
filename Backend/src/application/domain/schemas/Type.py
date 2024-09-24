from pydantic import BaseModel


class TypeSchema(BaseModel):
    id: int
    value: str

    class Config:
        from_attribute = True
