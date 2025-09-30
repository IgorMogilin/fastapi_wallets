from fastapi import FastAPI

from app.routers import wallets

app = FastAPI()
app_v1 = FastAPI(
    title='API Wallets v1',
    description='Позволяет получать информацию о кошельке и пополнять баланс.',
    version='1.0.0',
)

app_v1.include_router(wallets.router)

app.mount('/api/v1', app_v1)


@app.get('/')
def get_main_page() -> dict:
    """Корневой маршрут, подтверждающий что API работает."""
    return {
        'Документация доступна по адресу': 'http://127.0.0.1:8000/api/v1/docs'
    }
