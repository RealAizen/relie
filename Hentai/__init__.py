import logging 
from os import environ
from sys import exit
from telethon import TelegramClient
from pyrogram import Client
import logging

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create and configure the console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Create and configure the file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger

# Usage example
logger = setup_logger()
logger.info("Initializing the application")

#_____BASIC_________VARIABLE
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

LOG = logging.getLogger("Hentai")
LOG.setLevel(level=logging.INFO)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}
API_ID = environ.get('API_ID', 15849735)
API_HASH = environ.get('API_HASH', 'b8105dc4c17419dfd4165ecf1d0bc100')
BOT_TOKEN = environ.get('BOT_TOKEN', '6016198379:AAGMNXoPaIIKmf4DUXUOPfgVKY1EqWdOMRc')
#BOT_TOKEN = environ.get('BOT_TOKEN', '6108571944:AAEkzPB3zJUFLfFddBHY0DVnTeqQLrgHa6A')
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://cloud:OQl3YRgQV4dC5z6H@cluster0.bieyjxe.mongodb.net/?retryWrites=true&w=majority')
OWNER_ID = 720518864
DEV_USERS = "" #[1695508822, 5110399944]
LOG_CHANNEL = -1001300754259
BOT_USERNAME = "Heavenly_Premium_Bot"
NETWORK_CHANNELS_LINK = "https://t.me/c/1344295233/3020"
FSUB_CHANNEL_ID = -1001344295233

try:
    tsoheru = TelegramClient('Tsoheru', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
    psoheru = Client('PSoheru', API_ID, API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Hentai/plugins"))
except Exception as e:
    LOG.warn(f'Unable To Connect With Client\nReason:{e}')    
    exit()
