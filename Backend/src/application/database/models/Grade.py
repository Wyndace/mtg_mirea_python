from sqlalchemy.orm import Mapped, mapped_column

from .. import Base
from ...domain.schemas import GradeSchema


class Grade(Base):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[str]

    def to_read_model(self) -> GradeSchema:
        return GradeSchema(
            id=self.id,
            value=self.value,
        )
