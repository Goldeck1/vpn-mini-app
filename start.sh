#!/bin/bash

echo "🚀 Запуск VPN Mini App..."

# Запуск бэкенда
echo "📦 Запуск backend..."
cd backend
source venv/bin/activate 2>/dev/null || python -m venv venv && source venv/bin/activate
pip install -q -r requirements.txt 2>/dev/null

# Запуск API в фоне
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
API_PID=$!
echo "✅ API запущен (PID: $API_PID)"

# Запуск бота в фоне
python -m app.bot &
BOT_PID=$!
echo "✅ Бот запущен (PID: $BOT_PID)"

cd ../frontend

# Запуск фронтенда
echo "🎨 Запуск frontend..."
npm install 2>/dev/null
npm run dev &
FRONTEND_PID=$!
echo "✅ Frontend запущен (PID: $FRONTEND_PID)"

echo ""
echo "🎉 Все сервисы запущены!"
echo "   API: http://localhost:8000"
echo "   Frontend: http://localhost:5173"
echo ""
echo "Нажмите Ctrl+C для остановки"

wait
