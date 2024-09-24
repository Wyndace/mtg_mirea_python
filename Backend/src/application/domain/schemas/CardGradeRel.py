from pydantic import BaseModel


class CardGradeRelSchema(BaseModel):
    id: int
    card_id: int
    grade_id: int

    class Config:
        from_attribute = True
