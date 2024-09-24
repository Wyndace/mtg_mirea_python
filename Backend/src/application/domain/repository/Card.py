from ...utils.repository import SQLAlchemyRepository
from ...database.models import Card


class CardRepository(SQLAlchemyRepository):
    model = Card
