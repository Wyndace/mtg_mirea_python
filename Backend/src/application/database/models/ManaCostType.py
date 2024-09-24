from sqlalchemy.orm import Mapped, mapped_column

from .. import Base
from ...domain.schemas import ManaCostTypeSchema


class ManaCostType(Base):
    __tablename__ = "mana_cost_types"
    name: Mapped[str]
    code: Mapped[str] = mapped_column(primary_key=True)

    def to_read_model(self) -> ManaCostTypeSchema:
        return ManaCostTypeSchema(
            code=self.code,
            name=self.name,
        )
