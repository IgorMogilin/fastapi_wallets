from fastapi import APIRouter


router = APIRouter(
    prefix='/wallets',
    tags=['wallets'],
)


@router.get(
    '/',
)
async def get_wallets():
    return {'message': 'Wallets'}
