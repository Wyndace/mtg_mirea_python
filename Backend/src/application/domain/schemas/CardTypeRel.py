from pydantic import BaseModel


class CardTypeRelSchema(BaseModel):
    id: int
    card_id: int
    type_id: int

    class Config:
        from_attribute = True
