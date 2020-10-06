import os
import telebot
from decouple import config

from dotenv import load_dotenv

load_dotenv()

TOKEN =  os.environ.get("BOT_TOKEN")


bot = telebot.TeleBot(TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Buy', 'Sell')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Барахолока НУЛП. Продається все(майже). Please, make up your choice', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Купити':
        bot.send_message(message.chat.id, 'Функціоналу ще немає :/')
    elif message.text.lower() == 'Продати':
        bot.send_message(message.chat.id, '2:0. Теж не реалізовано')




bot.polling()