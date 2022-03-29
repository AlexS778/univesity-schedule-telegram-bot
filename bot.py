import telebot

import schedule
from bot_token import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Start":
        bot.send_message(message.chat.id, schedule.get_schedule())


bot.infinity_polling()
