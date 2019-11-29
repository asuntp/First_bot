
# Импортируем обработчики
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


# Добавляем логгирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# Функция greet_user будет вызаваться, когда пользователь напишет /start или подключится к боту в первый раз
#Параметря принято называть bot & update (должно быть как минимум 2 параметра)
def greet_user(bot, update):
    #bot.send_message(chat_id=update.message.chat_id, text='Hi!')
    text = 'Call /start'
    print(text)
    logging.info(text)
    update.message.reply_text(text)
    #Простейший способ ответа пользователю


def talk_to_me(bot, update):
    user_text = 'Hello {}! You wrote: {}'.format(update.message.chat.username, update.message.text)
    #bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    print(update.message)
    # эхобот ---отправляет пользователю тот текст который он написал
    update.message.reply_text(user_text)

def error(bot, update):
    logging.warning('Update "%s" caused error "%s"', bot, update.error)


# Функция которая соединяется с платформой telegram
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)
    logging.info('bot start')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) #Когда придет команда start выполнится функция
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_error_handler(error)

    mybot.start_polling()
    mybot.idle()

main()













