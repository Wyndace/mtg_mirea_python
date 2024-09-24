from ...utils.repository import SQLAlchemyRepository
from ...database.models import SubType


class SubTypeRepository(SQLAlchemyRepository):
    model = SubType
