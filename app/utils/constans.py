from fastapi import HTTPException, status


WALLET_NOT_FOUND = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Wallet not found'
            )
NOT_ENOUGH_BALANCE = HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not enough money'
            )
MAX_LENGTH_TITLE = 100
MIN_LENGTH_TITLE = 3
MAX_LENGTH_DESCRIPTION = 500
DEFAULT_BALANCE = 0.00
LIMITS_BALANCE = (10, 2)
MINIMAL_BALANCE = 0
