# Remember to use your own values from my.telegram.org!
from configparser import ConfigParser
from time import sleep

import telebot

parser = ConfigParser()
parser.read('behave.ini')
config = parser


def send_document(context, caption, document_name='page_source.html'):
    try:
        if document_name == 'page_source.html':
            with open("page_source.html", "w") as f:
                f.write(context.driver.page_source)
        image = context.driver.get_screenshot_as_png()
        bot = telebot.TeleBot(config['telegram']['telegram_token'])
        chat_id = config['telegram']['telegram_to']
        bot.send_photo(chat_id=chat_id, photo=image)
        bot.send_document(chat_id=chat_id, document=open(document_name, "rb"), caption=caption)
        bot.stop_bot()
    except Exception:
        raise RuntimeError(f'Telegram failed to send doc with message: {caption}')


def send_doc(caption, html):
    # html: r.text or str(soup)
    try:
        with open("page_source.html", "w") as f:
            f.write(html)
        bot = telebot.TeleBot(config['telegram']['telegram_token'])
        chat_id = config['telegram']['telegram_to']
        bot.send_document(chat_id=chat_id, document=open("page_source.html", "rb"), caption=caption)
        bot.stop_bot()
    except Exception:
        raise RuntimeError(f'Telegram failed to send doc with message: {caption}')


def send_image(image_name, caption):
    try:
        bot = telebot.TeleBot(config['telegram']['telegram_token'])
        chat_id = config['telegram']['telegram_to']
        bot.send_photo(chat_id=chat_id, photo=image_name, caption=caption)
        bot.stop_bot()
    except Exception:
        raise RuntimeError(f'Telegram failed to image with message: {caption}')


def send_message(message):
    for _ in range(3):
        try:
            bot = telebot.TeleBot(config['telegram']['telegram_token'])
            bot.send_message(chat_id=config['telegram']['telegram_to'], text=message)
            bot.stop_bot()
            break
        except Exception:
            raise RuntimeError(f'Telegram failed to send message: {message}')
