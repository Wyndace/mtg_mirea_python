from pydantic import BaseModel


class ManaCostTypeSchema(BaseModel):
    code: str
    type: str

    class Config:
        from_attribute = True


class ManaCostTypeCreateSchema(BaseModel):
    type: str
