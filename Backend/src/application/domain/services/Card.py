from typing import Type

from ..schemas.Card import CardSchema
from ...utils.repository import AbstractRepositoryDatabase


class CardService:
    def __init__(self, card_repository: Type[AbstractRepositoryDatabase]):
        self.card_repository = card_repository()

    def get_cards(self):
        return self.card_repository.find_all()

    def save_card(self, card: CardSchema):
        card_data = card.model_dump()
        return self.card_repository.add_one(card_data)
