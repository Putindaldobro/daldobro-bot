import os
import telebot
import openai

# Переменные из Railway (или .env)
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Инициализация бота и OpenAI
bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

# Хендлер на любое текстовое сообщение
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text

    try:
        # GPT-ответ
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # можно заменить на "gpt-4", если есть доступ
            messages=[{"role": "user", "content": user_text}]
        )
        reply = response.choices[0].message.content.strip()
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

# Запуск
if name == "__main__":
    print("DALDOBROBot запущен")
    bot.polling(none_stop=True)