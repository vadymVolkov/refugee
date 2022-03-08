import configparser
import telebot
from handler import Handler
import logging

telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60

config = configparser.ConfigParser()
config.read("config.ini")

API_TOKEN = config['main']['api_token']

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

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


@bot.message_handler(
    func=lambda mess: "Информация для тех кто потерялся или кого-то потерял" == mess.text,
    content_types=['text'])
def handle_text(message):
    handler.lost(message)


@bot.message_handler(
    func=lambda mess: "Полезная информация от Международного Штаба помощи украинцам" == mess.text,
    content_types=['text'])
def handle_text(message):
    handler.usefull_info_ihhu(message)


@bot.message_handler(
    func=lambda mess: "Полезная информация" == mess.text,
    content_types=['text'])
def handle_text(message):
    handler.usefull_info(message)

@bot.message_handler(
    func=lambda mess: "Вернуться к списку стран" == mess.text,
    content_types=['text'])
def handle_text(message):
    handler.border_crossing(message)

bot.remove_webhook()

bot.polling(none_stop=True, interval=0)
