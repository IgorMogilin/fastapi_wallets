from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field


class WalletCreate(BaseModel):
    """
    Схема для создания и обновления.
    Используется в POST и PUT-запросах.
    """

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
    uuid: UUID = Field(
        ...,
        description='Уникальный номер идентификатор кошелька',
    )
    balance: Decimal = Field(
        default=0.00,
        ge=0,
        description='Текущий баланс',
    )


class WalletResponse(WalletCreate):
    """
    Схема для ответа с данными кошелька.
    Используется в GET-запросах.
    """

    id: int = Field(..., description='ID кошелька в базе данных')
    executing_date: datetime | None = Field(
        None,
        description='Дата последней операции (снятие/пополнение)'
    )
