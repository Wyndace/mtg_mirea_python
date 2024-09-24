from pydantic import BaseModel


class GradeSchema(BaseModel):
    id: int
    name: str
    action: str
    description: str

    class Config:
        from_attribute = True
