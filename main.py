import os
import telebot
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text

    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "https://daldobro.xyz",  # укажи свой домен, если хочешь
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",  # можно заменить на gpt-4, mistral, claude и т.д.
            "messages": [
                {"role": "user", "content": user_text}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()

        reply = result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        reply = f"Ошибка: {str(e)}"

    bot.reply_to(message, reply)

if __name__ == "__main__":
    print("DALDOBROBot запущен через OpenRouter")
    bot.polling(non_stop=True)