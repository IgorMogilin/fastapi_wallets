from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_depends import get_async_db
from app.models.wallets import Wallet
from app.schemas.wallets import OperationType, WalletOperation, WalletResponse
from app.utils.constans import NOT_ENOUGH_BALANCE, WALLET_NOT_FOUND

router = APIRouter(
    prefix='/wallets',
    tags=['wallets'],
)


@router.get(
    '/{wallet_uuid}',
    response_model=WalletResponse
)
async def get_wallet_info(
    wallet_uuid: UUID,
    db: AsyncSession = Depends(get_async_db)
) -> WalletResponse:
    """Функция для получения информации о кошельке."""
    wallet = await db.scalar(
        select(Wallet)
        .where(Wallet.uuid == wallet_uuid)
    )
    if not wallet:
        raise WALLET_NOT_FOUND
    return wallet


@router.post(
    '/{wallet_uuid}/operation',
    response_model=WalletResponse,
    status_code=status.HTTP_200_OK,
)
async def wallet_operation(
    wallet_uuid: UUID,
    operation: WalletOperation,
    db: AsyncSession = Depends(get_async_db),
) -> WalletResponse:
    """Функция для обновления данных кошелька."""
    async with db.begin():
        wallet = await db.scalar(
            select(Wallet)
            .where(Wallet.uuid == wallet_uuid)
            .with_for_update()
        )
        if not wallet:
            raise WALLET_NOT_FOUND
        if operation.operation_type == OperationType.WITHDRAW:
            if wallet.balance < operation.amount:
                raise NOT_ENOUGH_BALANCE
        if operation.operation_type == OperationType.DEPOSIT:
            wallet.balance += operation.amount
        else:
            wallet.balance -= operation.amount
        wallet.executing_date = datetime.now()
    await db.refresh(wallet)
    return wallet
