import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from calc import arithmetic
from sun_sistem import planet
from picture import rockets
from greeting import greet_user
from eho import talk_to_me
from now_distance import now
#from errors import error

# Добавляем логгирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

# Функция которая соединяется с платформой telegram
def main():
    updater = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('bot start')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) #Когда придет команда /start выполнится функция
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(CommandHandler('now', now))
    dp.add_handler(CommandHandler('calc', arithmetic))
    dp.add_handler(CommandHandler('rocket', rockets))
    dp.add_handler(MessageHandler(Filters.regex('^(Команды)$'), greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    #dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()













