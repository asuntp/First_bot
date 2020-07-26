
# Импортируем обработчики
from glob import glob
import logging
from random import choice, randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import settings
from glob import glob

# Добавляем логгирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# Функция greet_user будет вызаваться, когда пользователь напишет /start или подключится к боту в первый раз
#Параметря принято называть bot & update (должно быть как минимум 2 параметра)
def greet_user(bot, update):
    #text = 'Hello, you can rule some command and get answer, like distance from Earth and selectes planet on a input date: /Moon, /Mars, /Jupiter, /Saturn, /Venus, /Mercury, /Uranus '
    text = '''Привет, ты можешь набрать команду состоящую из названия планеты и через пробел
      год в котором ты хочешь получить расстояние между Землёй и заданным небесным телом. 
      Названия планет: Mars, Jupiter, Saturn, Venus, Mercury, Uranus, Moon. . Команда выполняется 
      в виде: /planet Mars 1981. По команде /calc доступны арифметические действия над двумя 
      числами. Пример команды /calc 25 + 35
      '''
    print(text)
    logging.info(text)
    update.message.reply_text(text)
    #Простейший способ ответа пользователю


def talk_to_me(bot, update):

    text = 'Привет {}, ты написал {}.'.format(update.message.chat.username, update.message.text)
    update.message.reply_text(text)
    print(update.message)

    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                   update.message.chat.id, update.message.text)
    # эхобот ---отправляет пользователю тот текст который он написал


def planet(bot, update):
    try:
        user_text = update.message.text
        user_text = user_text.split()
        planet = user_text[1]
        ear = (user_text[2])
        if type(user_text[1]) != str:
            update.message.reply_text('Планеты нужно писать буквами')
        elif not user_text[2].isdigit():
            update.message.reply_text('Год записывается цифрами')
        elif 1 < len(user_text) < 3 or len(user_text) > 3:
            update.message.reply_text('Введите команду правильно')
        elif planet == 'Mars':
            distance = int(ephem.Mars(ear).earth_distance) * 149597870
            user_text = 'В {} году расстояние между Землей и Марсом было (будет): {} k.m.'.format(ear, distance)
        elif planet == 'Moon':
            distance = int(ephem.Moon(ear).earth_distance) * 149597870
            user_text = 'В {} году расстояние между Землей и Луной было (будет): {} k.m.'.format(ear, distance)
        elif planet == 'Jupiter':
            distance = int(ephem.Jupiter(ear).earth_distance) * 149597870
            user_text = 'В {} году расстояние между Землей и Юпитером было (будет): {} k.m.'.format(ear, distance)
        elif planet == 'Saturn':
            distance = int(ephem.Saturn(ear).earth_distance) * 149597870
            user_text = 'В {} году расстояние между Землей и Сатурном было (будет): {} k.m.'.format(ear, distance)
        elif planet == 'Venus':
            distance = int(ephem.Venus(ear).earth_distance) * 149597870
            user_text = 'В {} году расстояние между Землей и Венерой было (будет): {} k.m.'.format(ear, distance)
        elif planet == 'Mercury':
            distance = int(ephem.Mercury(ear).earth_distance) * 149597870
            user_text = 'В {} году расстояние между Землей и Меркурием было (будет): {} k.m.'.format(ear, distance)
        elif planet == 'Uranus':
            distance = int(ephem.Uranus(ear).earth_distance) * 149597870
            user_text = 'В {} году расстояние между Землей и Ураном было (будет): {} k.m.'.format(ear, distance)
        else:
            update.message.reply_text("Введите правильное название небесного тела")
        update.message.reply_text(user_text)
    except TypeError:
        update.message.reply_text("По команде /start вызываются правильные примеры команд")

def arithmetic(bot, update):
    try:
        user_text = update.message.text
        user_text = user_text.split()
        user_text[1] = float(user_text[1])
        user_text[3] = float(user_text[3])
        if type(user_text[1]) != float or type(user_text[3]) != float:
            update.message.reply_text('Действия производятся только над цифрами')

        elif 1 < len(user_text) < 4 or len(user_text) > 4:
            update.message.reply_text('Введите команду правильно')
        elif user_text[2] == '+':
            update.message.reply_text(user_text[1] + user_text[3])
        elif user_text[2] == '-':
            update.message.reply_text(user_text[1] - user_text[3])
        elif user_text[2] == '*':
            update.message.reply_text(user_text[1] * user_text[3])
        elif user_text[2] == '/':
            update.message.reply_text(user_text[1] / user_text[3])
        else:
            update.message.reply_text('Что то пошло не так')
    except ValueError:
        update.message.reply_text('Действия производятся только над цифрами')

def rockets(bot, update, context):
    rock_img_list = glob('images/rocket*.jp*g')
    rock_img_filename = choice(rock_img_list)
    chat_id =update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(rock_img_filename, "rb"))


def error(bot, update):
    logging.warning('Update "%s" caused error "%s"', bot, update.error)

# Функция которая соединяется с платформой telegram
def main():
    updater = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('bot start')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) #Когда придет команда start выполнится функция
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(CommandHandler('calc', arithmetic))
    dp.add_handler(CommandHandler('rocket', rockets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    #dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()













