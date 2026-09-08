from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    documents: Mapped[list["Document"]] = relationship(
        back_populates="owner"
    )


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    filename: Mapped[str] = mapped_column(
        String(255)
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    owner: Mapped["User"] = relationship(
        back_populates="documents"
    )