from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import settings
from app.db.session import engine
from app.models.user import Base


app = FastAPI(title="VPN Mini App API", version="1.0.0")

# CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роуты
app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    """Создание таблиц БД при старте"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("✅ БД инициализирована")
    print(f"🤖 Бот токен: {settings.telegram_bot_token[:20]}...")
    print(f"🌐 Frontend URL: {settings.frontend_url}")


@app.get("/")
async def root():
    return {"message": "VPN Mini App API", "status": "running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
