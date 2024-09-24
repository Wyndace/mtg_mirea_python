from ...utils.repository import SQLAlchemyRepository
from ...database.models import Grade


class GradeRepository(SQLAlchemyRepository):
    model = Grade
