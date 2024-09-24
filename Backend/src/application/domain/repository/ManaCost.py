from ...utils.repository import SQLAlchemyRepository
from ...database.models import ManaCost


class ManaCostRepository(SQLAlchemyRepository):
    model = ManaCost
