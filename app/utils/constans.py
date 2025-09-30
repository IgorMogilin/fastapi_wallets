from fastapi import HTTPException, status


WALLET_NOT_FOUND = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Wallet not found'
            )
NOT_ENOUGH_BALANCE = HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not enough money'
            )
