from datetime import datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field

from app.utils.constans import (
    DEFAULT_BALANCE,
    MAX_LENGTH_TITLE,
    MAX_LENGTH_DESCRIPTION,
    MIN_LENGTH_TITLE,
    MINIMAL_BALANCE,
)


class OperationType(str, Enum):
    """Схема для выбора типа операции."""

    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class WalletCreate(BaseModel):
    """Схема для будущей реализации логики создания кошелька."""

    title: str = Field(
        ...,
        min_length=MIN_LENGTH_TITLE,
        max_length=MAX_LENGTH_TITLE,
        description='Название кошелька.',
    )
    description: str | None = Field(
        None,
        max_length=MAX_LENGTH_DESCRIPTION,
        description='Описание кошелька (до 500 символов)',
    )
    balance: Decimal = Field(
        default=DEFAULT_BALANCE,
        ge=MINIMAL_BALANCE,
        description='Начальный баланс',
    )


class WalletResponse(BaseModel):
    """Схема для ответа с данными кошелька. Используется в GET-запросах."""

    id: int = Field(..., description='ID кошелька в базе данных')
    title: str = Field(
        ...,
        description='Название кошелька.',
    )
    description: str | None = Field(
        None,
        description='Описание кошелька',
    )
    uuid: UUID = Field(
        ...,
        description='Уникальный идентификатор кошелька',
    )
    balance: Decimal = Field(
        ...,
        description='Текущий баланс',
    )
    executing_date: datetime | None = Field(
        None,
        description='Дата последней операции (снятие/пополнение)'
    )


class WalletOperation(BaseModel):
    """Схема для изменения баланса кошелька."""

    operation_type: OperationType = Field(
        ...,
        description='Тип операции'
    )
    amount: Decimal = Field(
        ...,
        ge=MINIMAL_BALANCE,
        description='Сумма операции'
    )
