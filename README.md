# 🚀 VPN Mini App

Telegram Mini App для продажи VPN-подписок.

## 📁 Структура проекта

```
vpn-mini-app/
├── backend/          # FastAPI бэкенд
│   ├── app/
│   │   ├── api/      # API роуты
│   │   ├── core/     # Конфигурация
│   │   ├── db/       # БД сессии
│   │   ├── models/   # SQLAlchemy модели
│   │   ├── schemas/  # Pydantic схемы
│   │   ├── services/ # Бизнес-логика
│   │   ├── main.py   # Точка входа
│   │   └── bot.py    # Telegram бот
│   ├── tests/
│   └── requirements.txt
└── frontend/         # React + TypeScript фронтенд
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── hooks/
    │   ├── services/
    │   ├── types/
    │   └── assets/
    └── public/
```

## 🚀 Быстрый старт

### 1. Бэкенд

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Настройте .env (уже создан)
# Запустите миграции БД (если нужно)

# Запуск API
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Запуск бота (в отдельном терминале)
python -m app.bot
```

### 2. Фронтенд

```bash
cd frontend
npm install
npm run dev
```

### 3. Настройка бота

1. Откройте [@BotFather](https://t.me/BotFather)
2. `/newapp` → выберите вашего бота
3. Укажите URL: `https://your-domain.com` (или ngrok для локальной разработки)
4. Или используйте `/setdomain` для установки Web App URL

## 🔧 Переменные окружения

### Backend (.env)
```
TELEGRAM_BOT_TOKEN=your_bot_token
DATABASE_URL=postgresql://user:password@localhost:5432/vpn_db
SECRET_KEY=your-secret-key
FRONTEND_URL=http://localhost:5173
```

## 📦 API Endpoints

- `POST /api/users` - Создать пользователя
- `GET /api/users/{telegram_id}` - Получить пользователя
- `POST /api/subscriptions` - Создать подписку
- `GET /api/users/{user_id}/subscriptions` - Подписки пользователя

## 🛠 Технологии

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL, python-telegram-bot
- **Frontend**: React 18, TypeScript, Vite, Telegram WebApp SDK
