import logging
import asyncio
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from app.core.config import settings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    logger.info(f"Пользователь {user.id} ({user.first_name}) вызвал /start")

    # Создаем клавиатуру с кнопкой для открытия Mini App
    keyboard = [
        [InlineKeyboardButton(
            "🛒 Открыть магазин VPN",
            web_app=WebAppInfo(url=settings.frontend_url)
        )],
        [InlineKeyboardButton(
            "🌐 Открыть в браузере",
            url=settings.frontend_url
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        await update.message.reply_text(
            f"👋 Привет, {user.first_name}!\n\n"
            f"🚀 Добро пожаловать в VPN Mini App!\n\n"
            f"Нажми на кнопку ниже, чтобы выбрать тариф и оформить подписку.",
            reply_markup=reply_markup,
        )
    except Exception as e:
        logger.error(f"Ошибка отправки сообщения: {e}")
        # Fallback - просто ссылка
        await update.message.reply_text(
            f"👋 Привет, {user.first_name}!\n\n"
            f"🚀 Добро пожаловать в VPN Mini App!\n\n"
            f"Открой приложение: {settings.frontend_url}"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    await start(update, context)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик обычных сообщений"""
    await update.message.reply_text(
        "Используйте меню или команду /start для взаимодействия с ботом."
    )


def main():
    """Запуск бота"""
    logger.info("Запуск бота...")

    application = Application.builder().token(settings.telegram_bot_token).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
