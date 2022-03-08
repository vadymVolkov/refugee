import configparser
import telebot
from handler import Handler
import logging
import fastapi
import telebot

config = configparser.ConfigParser()
config.read("config.ini")

API_TOKEN = config['main']['api_token']



WEBHOOK_HOST = '3.80.107.93'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '3.80.107.93'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key

# Quick'n'dirty SSL certificate generation:
#
# openssl genrsa -out webhook_pkey.pem 2048
# openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
#
# When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
# with the same value in you put in WEBHOOK_HOST

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

app = fastapi.FastAPI()

handler = Handler(bot)

# Process webhook calls
@app.post(f'/{API_TOKEN}/')
def process_webhook(update: dict):
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return

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


# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))


import uvicorn
uvicorn.run(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    ssl_certfile=WEBHOOK_SSL_CERT,
    ssl_keyfile=WEBHOOK_SSL_PRIV
)
