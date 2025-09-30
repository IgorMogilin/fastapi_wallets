from datetime import datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class OperationType(str, Enum):
    """Схема для выбора типа операции."""

    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class WalletCreate(BaseModel):
    """Схема для будущей реализации логики создания кошелька."""

    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description='Название кошелька.',
    )
    description: str | None = Field(
        None,
        max_length=500,
        description='Описание кошелька (до 500 символов)',
    )
    balance: Decimal = Field(
        default=0.00,
        ge=0,
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
        ge=0,
        description='Сумма операции'
    )
