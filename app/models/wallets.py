from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import UUID as UUID_field
from sqlalchemy import DateTime, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.utils.constans import (
    DEFAULT_BALANCE,
    LIMITS_BALANCE,
    MAX_LENGTH_TITLE,
)


class Wallet(Base):
    """Модель кошелька."""

    __tablename__ = 'wallets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(
        String(MAX_LENGTH_TITLE),
        nullable=False
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text(),
        nullable=True,
    )
    uuid: Mapped[UUID] = mapped_column(
        UUID_field(as_uuid=True),
        nullable=False,
        unique=True,
        index=True,
        default=uuid4,
    )
    balance: Mapped[Decimal] = mapped_column(
        Numeric(*LIMITS_BALANCE),
        default=DEFAULT_BALANCE,
    )
    executing_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        nullable=True,
    )
