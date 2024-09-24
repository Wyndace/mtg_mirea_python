from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .. import Base
from ...domain.schemas import ManaCostSchema


class ManaCost(Base):
    __tablename__ = "mana_costs"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    card_id: Mapped[int] = mapped_column(ForeignKey("cards.id", ondelete="CASCADE"), nullable=False)
    mana_cost_type_code: Mapped[str] = mapped_column(ForeignKey("mana_cost_types.code", ondelete="CASCADE"),
                                                     nullable=False)
    count: Mapped[int]

    def to_read_model(self) -> ManaCostSchema:
        return ManaCostSchema(
            id=self.id,
            card_id=self.card_id,
            mana_cost_type_code_id=self.mana_cost_type_code,
            count=self.count,
        )
