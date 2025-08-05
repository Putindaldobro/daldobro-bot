import os
import telebot
import openai

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

# Хендлер сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}]
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Ошибка: {str(e)}"

    bot.reply_to(message, reply)

# Запуск бота
if name == "__main__":
    print("DALDOBROBot запущен")
    bot.polling(non_stop=True)