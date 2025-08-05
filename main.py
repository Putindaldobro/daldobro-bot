import os
import telebot
import openai

# Получаем токены из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Проверка на наличие ключей
if not BOT_TOKEN or not OPENAI_API_KEY:
    raise ValueError("BOT_TOKEN или OPENAI_API_KEY не заданы!")

# Инициализация бота и клиента OpenAI
bot = telebot.TeleBot(BOT_TOKEN)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text

    try:
        response = client.chat.completions.create(
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