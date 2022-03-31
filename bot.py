import telebot
from telebot import types

# from bot_token import BOT_TOKEN
from schedule import ScheduleToday

bot = telebot.TeleBot("5125219826:AAGM_KfCH-PvDgqyroyv2OF32QFSMyfDr28")

keyboard = types.ReplyKeyboardMarkup()
b1 = types.InlineKeyboardButton('button', callback_data='foo')
keyboard.add(b1)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Start":
        bot.send_message(message.chat.id, ScheduleToday())
    if message.text == 'meow':
        bot.send_message(message.chat.id, 'text', reply_markup=keyboard)

bot.infinity_polling()
