import os
import telebot
from openai import OpenAI

# Получаем переменные среды
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Инициализация бота и клиента OpenRouter
bot = telebot.TeleBot(BOT_TOKEN)

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://daldobro.xyz",  # или свой сайт
        "X-Title": "DALDOBROBot"
    }
)

# Обработка всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text

    try:
        response = client.chat.completions.create(
    model="anthropic/claude-3-haiku",
    messages=[{"role": "user", "content": user_text}]
)
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Ошибка: {str(e)}"

    bot.reply_to(message, reply)

# Запуск бота
if __name__ == "__main__":
    print("🤖 DALDOBROBot запущен через OpenRouter")
    bot.polling(non_stop=True, skip_pending=True)