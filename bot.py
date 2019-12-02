
# Импортируем обработчики
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem

# Добавляем логгирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# Функция greet_user будет вызаваться, когда пользователь напишет /start или подключится к боту в первый раз
#Параметря принято называть bot & update (должно быть как минимум 2 параметра)
def greet_user(bot, update):
    #text = 'Hello, you can rule some command and get answer, like distance from Earth and selectes planet on a input date: /Moon, /Mars, /Jupiter, /Saturn, /Venus, /Mercury, /Uranus '
    text = 'Привет, ты можешь набрать команду состоящую из названия планеты и через пробел  год в котором ты хочешь получить расстояние между Землёй и заданным небесным телом. Названия планет: Mars, Jupiter, Saturn, Venus, Mercury, Uranus, Moon. Расстояние указывается в астрономических единицах (1 a.e. = 149 600 000 км.). Команда выполняется в виде: /planet Mars 1981'
    print(text)
    logging.info(text)
    update.message.reply_text(text)
    #Простейший способ ответа пользователю


def talk_to_me(bot, update):
    #text = 'Привет {}, ты написал {}.'.format(update.message.username, update.message.text)
    #update.message.reply_text(text)
    user_text = update.message.text
    user_text = user_text.split()
    body = user_text[0]
    ear = abs(int(user_text[1]))
    planet_dict = {'Mars': 'Mars', 'Moon': 'Moon', 'Jupiter': 'Jupiter', 'Saturn': 'Saturn', 'Venus': 'Venus', 'Mercury': 'Mercury', 'Uranus': 'Uranus'}

    if body in planet_dict:
        temp_body = planet_dict.get(body)planet_dict.get(body)
        print(temp_body)
        distance = ephem.temp_body(ear).earth_distance
        print(distance)
        user_text1 = 'В {} году расстояние между Землей и {} было (будет): {}'.format(ear, planet, distance)
        update.message.reply_text(user_text1)
    else:
        update.message.reply_text("Введите правильное название небесного тела")
    print(update.message)

    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                 update.message.chat.id, update.message.text)
    # эхобот ---отправляет пользователю тот текст который он написал
    #update.message.reply_text(user_text1)


def planet(bot, update):
    user_text2 = update.message.text
    user_text2 = user_text2.split()
    planet1 = user_text2[1]
    ear = (user_text2[2])

    if planet1 == 'Mars':
        distance = ephem.Mars(ear).earth_distance
        user_text2 = 'В {} году расстояние между Землей и Марсом было (будет): {} a.e.'.format(ear, distance)
    elif planet1 == 'Moon':
        distance = ephem.Moon(ear).earth_distance
        user_text2 = 'В {} году расстояние между Землей и Луной было (будет): {} a.e.'.format(ear, distance)
    elif planet1 == 'Jupiter':
        distance = ephem.Jupiter(ear).earth_distance
        user_text2 = 'В {} году расстояние между Землей и Юпитером было (будет): {} a.e.'.format(ear, distance)
    elif planet1 == 'Saturn':
        distance = ephem.Saturn(ear).earth_distance
        user_text2 = 'В {} году расстояние между Землей и Сатурном было (будет): {} a.e.'.format(ear, distance)
    elif planet1 == 'Venus':
        distance = ephem.Venus(ear).earth_distance
        user_text2 = 'В {} году расстояние между Землей и Венерой было (будет): {} a.e.'.format(ear, distance)
    elif planet1 == 'Mercury':
        distance = ephem.Mercury(ear).earth_distance
        user_text2 = 'В {} году расстояние между Землей и Меркурием было (будет): {} a.e.'.format(ear, distance)
    elif planet1 == 'Uranus':
        distance = ephem.Uranus(ear).earth_distance
        user_text2 = 'В {} году расстояние между Землей и Ураном было (будет): {} a.e.'.format(ear, distance)
    else:
        update.message.reply_text("Введите правильное название небесного тела")
    update.message.reply_text(user_text2)

def error(bot, update):
    logging.warning('Update "%s" caused error "%s"', bot, update.error)

# Функция которая соединяется с платформой telegram
def main():
    updater = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('bot start')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) #Когда придет команда start выполнится функция
    dp.add_handler(CommandHandler('planet', planet)) #Когда придет команда start выполнится функция
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    #dp.add_handler(MessageHandler(Filters.text, planet))
    #dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()













