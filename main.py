import os
import telebot
import openai

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenRouter конфигурация
openai.api_key = OPENAI_API_KEY.strip()
openai.base_url = "https://openrouter.ai/api/v1"
openai.api_type = "openai"
openai.api_key_prefix = "Bearer"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}]
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Ошибка: {str(e)}"
    
    bot.reply_to(message, reply)

if name == "__main__":
    print("DALDOBROBot запущен")
    bot.polling(none_stop=True)