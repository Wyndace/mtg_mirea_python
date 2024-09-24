from ...utils.repository import SQLAlchemyRepository
from ...database.models import ManaCostType


class ManaCostTypeRepository(SQLAlchemyRepository):
    model = ManaCostType
