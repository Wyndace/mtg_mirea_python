from pydantic import BaseModel


class CardSubTypeRelSchema(BaseModel):
    id: int
    card_id: int
    sub_type_id: int

    class Config:
        from_attribute = True
