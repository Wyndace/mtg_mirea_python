from pydantic import BaseModel


class CardSchema(BaseModel):
    id: int
    name: str
    action: str
    description: str

    class Config:
        from_attribute = True
