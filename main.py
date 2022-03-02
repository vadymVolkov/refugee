import configparser
import telebot
import controller
from handler import Handler

config = configparser.ConfigParser()
config.read("config.ini")

API_TOKEN = config['main']['api_token']

bot = telebot.TeleBot(API_TOKEN)
handler = Handler(bot)


@bot.message_handler(commands=['start'])
def handle_text(message):
    handler.main_menu(message)

@bot.message_handler(
    func=lambda mess: "В главное меню" == mess.text,
    content_types=['text'])
def handle_text(message):
    handler.main_menu(message)

@bot.message_handler(
    func=lambda mess: "Информация по пересечению границы" == mess.text,
    content_types=['text'])
def handle_text(message):
    handler.border_crossing(message)


bot.polling(none_stop=True, interval=0)
