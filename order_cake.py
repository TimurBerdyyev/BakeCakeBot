from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
import os
import requests
import telegram
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
telegram_token = os.environ["TG_TOKEN"]
tg_chat_id = os.environ["TG_CHAT_ID"]
bot = telegram.Bot(token=telegram_token)


def send_image(cake_image, cake_name, cake_description, cake_price, cake_weight):
    """Опубликовать картинку торта с описанием и ценой"""
    path_to_image = Path('images', cake_image)
    url = f"https://api.telegram.org/bot{telegram_token}/sendPhoto"
    files = {}
    with open(path_to_image, 'rb') as image:
        files["photo"] = image
        params = {"chat_id": tg_chat_id, "caption": f"{cake_name}\n{cake_description}\n{cake_price} руб / {cake_weight} кг"}
        requests.get(url, params=params, files=files)


cakes = [
    {
        'cake_name': 'Чизкейк',
        'cake_image': 'cheescake.jpg',
        'cake_description': 'нежный чизкейк с кокосовым пудингом, арахисом и кокосовыми хлопьями',
        'cake_price': 5200,
        'cake_weight': 2500
    },
    {
        'cake_name': 'Вишневый торт',
        'cake_image': 'cherry_cake.jpg',
        'cake_description': 'медово-кокосовый торт, без глютена, со сметанным кремом, вишневым джемом и свежими ягодами',
        'cake_price': 4300,
        'cake_weight': 2.4
    },
    {
        'cake_name': 'Шоколадный бисквит',
        'cake_image': 'chocolate_biscuit.jpg',
        'cake_description': 'шоколадный бисквит с шоколадным муссом, орехом пекан и карамелью',
        'cake_price': 5300,
        'cake_weight': 2.4
    },
    {
        'cake_name': 'Шоколадная бомба',
        'cake_image': 'chocolate_bomb.jpg',
        'cake_description': 'шоколадный бисквит с шоколадным крем-чизом, черничным джемом и миксом свежих ягод',
        'cake_price': 6150,
        'cake_weight': 2.8
    },
    {
        'cake_name': 'Малиново-йогуртовый чизкейк',
        'cake_image': 'raspberry_yogurt.jpg',
        'cake_description': 'подушка из брауни, незапеченый чизкейк с бельгийским шоколадом и малиной',
        'cake_price': 4800,
        'cake_weight': 1.9
    },
    {
        'cake_name': 'Ванильный бисквит',
        'cake_image': 'vanilla_cake.jpg',
        'cake_description': 'нежный бисквит с малиновым кремом и миксом свежих ягод',
        'cake_price': 5000,
        'cake_weight': 2.4
    }
]

def main():
    for cake in cakes:
        send_image(cake['cake_image'], cake['cake_name'], cake['cake_description'], cake['cake_price'],
                   cake['cake_weight'])


if __name__ == "__main__":
    main()
