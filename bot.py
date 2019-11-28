
# Импортируем обработчики
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


# Добавляем логгирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filname='bot.log')




# Функция greet_user будет вызаваться, когда пользователь
def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)

    print(update.message)
    update.message.reply_text(user_text) #эхобот ---отправляет пользователю тот текст который он написал




# Функция которая соединяется с платформой telegram
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()













