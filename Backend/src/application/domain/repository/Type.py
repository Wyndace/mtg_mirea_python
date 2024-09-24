from ...utils.repository import SQLAlchemyRepository
from ...database.models import Type


class TypeRepository(SQLAlchemyRepository):
    model = Type
