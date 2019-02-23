
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

    # Функция, которая соединяется с платформой Telegram, "тело" нашего бота

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
    
def main():
    mybot = Updater("729888119:AAFIL2l9S2sddrBg0YRDg186y5NBHftNsCg", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()    
main()
