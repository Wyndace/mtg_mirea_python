from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from ...database import Base


class Card2Grade(Base):
    __tablename__ = "card_2_grade_rels"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    card_id: Mapped[int] = ForeignKey("cards.id", ondelete="CASCADE")
    grade_id: Mapped[int] = ForeignKey("grades.id", ondelete="CASCADE")
