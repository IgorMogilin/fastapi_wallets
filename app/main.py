from fastapi import FastAPI

from app.routers import wallets


app = FastAPI()
app_v1 = FastAPI(
    title='API v1',
    version='1.0.0',
)

app_v1.include_router(wallets.router)

app.mount('/api/v1', app_v1)
