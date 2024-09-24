from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Type, ManaCost, SubType, Card2Grade
from .. import Base
from ...domain.schemas import CardSchema


class Card(Base):
    __tablename__ = "cards"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    action: Mapped[str]
    description: Mapped[str]

    grades: Mapped[list["Card2Grade"]] = relationship(
        back_populates="card",
    )

    types: Mapped[list["Type"]] = relationship(
        back_populates="card",
    )

    subtypes: Mapped[list["SubType"]] = relationship(
        back_populates="card",
    )

    mana_costs: Mapped[list["ManaCost"]] = relationship(
        back_populates="card",
        secondary="mana_cost_type",
    )

    def to_read_model(self) -> CardSchema:
        return CardSchema(
            id=self.id,
            name=self.name,
            action=self.action,
            description=self.description,
        )
