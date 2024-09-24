from typing import Type

from ..schemas import ManaCostType
from ...utils.repository import AbstractRepositoryDatabase


class ManaCostTypeService:
    def __init__(self, type_repository: Type[AbstractRepositoryDatabase]):
        self.type_repository = type_repository()

    def get_types(self):
        return self.type_repository.find_all()

    def save_mana_cost_type(self, mana_cost_type: ManaCostType):
        mana_cost_data = mana_cost_type.model_dump()
        return self.type_repository.add_one(mana_cost_data)
