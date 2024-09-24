from sqlalchemy.orm import Mapped, mapped_column

from .. import Base
from ...domain.schemas import SubTypeSchema


class SubType(Base):
    __tablename__ = "sub_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[str]

    def to_read_model(self) -> SubTypeSchema:
        return SubTypeSchema(
            id=self.id,
            value=self.value,
        )
