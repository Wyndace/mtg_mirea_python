from pydantic import BaseModel


class ManaCostSchema(BaseModel):
    id: int
    card_id: int
    mana_cost_type_code_id: str
    count: int

    class Config:
        from_attribute = True
