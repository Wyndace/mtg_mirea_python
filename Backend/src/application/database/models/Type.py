from sqlalchemy.orm import Mapped, mapped_column

from .. import Base
from ...domain.schemas import TypeSchema


class Type(Base):
    __tablename__ = "types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[str]

    def to_read_model(self) -> TypeSchema:
        return TypeSchema(
            id=self.id,
            value=self.value,
        )
