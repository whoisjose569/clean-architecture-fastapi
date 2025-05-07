import sqlalchemy as sa
from src.infra.db.settings.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    age: Mapped[int] = mapped_column(sa.Integer, nullable=False)
