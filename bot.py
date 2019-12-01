
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
    text = 'Привет, ты можешь набрать команду состоящуую из названия планеты и через пробел  год в котором ты хочешь получить расстояние между Землёй и заданным небесным телом. Названия планет: Mars, Jupiter, Saturn, Venus, Mercury, Uranus, Moon. Расстояние указывается в астрономических единицах (1 a.e. = 149 600 000 км.). Команда выполняется в виде: Mars 1981'
    print(text)
    logging.info(text)
    update.message.reply_text(text)
    #Простейший способ ответа пользователю


def talk_to_me(bot, update):
    user_text = update.message.text
    user_text = user_text.split()
    planet = user_text[0]
    ear = abs(int(user_text[1]))

    if planet == 'Mars':
        distance = ephem.Mars(ear).earth_distance
        user_text1 = 'В {} году расстояние между Землей и Марсом было (будет): {}'.format(ear, distance)
    elif planet == 'Moon':
        distance = ephem.Moon(ear).earth_distance
        user_text1 = 'В {} году расстояние между Землей и Луной было (будет): {}'.format(ear, distance)
    elif planet == 'Jupiter':
        distance = ephem.Jupiter(ear).earth_distance
        user_text1 = 'В {} году расстояние между Землей и Юпитером было (будет): {}'.format(ear, distance)
    elif planet == 'Saturn':
        distance = ephem.Saturn(ear).earth_distance
        user_text1 = 'В {} году расстояние между Землей и Сатурном было (будет): {}'.format(ear, distance)
    elif planet == 'Venus':
        distance = ephem.Venus(ear).earth_distance
        user_text1 = 'В {} году расстояние между Землей и Венерой было (будет): {}'.format(ear, distance)
    elif planet == 'Mercury':
        distance = ephem.Mercury(ear).earth_distance
        user_text1 = 'В {} году расстояние между Землей и Меркурием было (будет): {}'.format(ear, distance)
    elif planet == 'Uranus':
        distance = ephem.Uranus(ear).earth_distance
        user_text1 = 'В {} году расстояние между Землей и Ураном было (будет): {}'.format(ear, distance)
    else:
        update.message.reply_text("Введите правильное название небесного тела")

    #print(update.message)

    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                 update.message.chat.id, update.message.text)
    # эхобот ---отправляет пользователю тот текст который он написал
    update.message.reply_text(user_text1)


def mars(bot, update):
    update.message.reply_text('Введите год')
    ear = update.message.text
    distance = ephem.Mars(ear).earth_distance
    user_text1 = 'В {} году расстояние между Землей и Марсом было: {}'.format(ear, distance)
    update.message.reply_text(user_text1)

    #data = {update.message.text: ephem.Mars(update.message.text).earth_distance}

    #data = {'1900 a.c.': ephem.Mars(1900).earth_distance, '1910 a.c.': ephem.Mars(1910).earth_distance,
    #        '1920 a.c.': ephem.Mars(1920).earth_distance, '1930 a.c.': ephem.Mars(1930).earth_distance,
    #        '1940 a.c.': ephem.Mars(1940).earth_distance, '1950 a.c.': ephem.Mars(1950).earth_distance}
    #update.message.reply_text({update.message.text: ephem.Mars(update.message.text).earth_distance})




def error(bot, update):
    logging.warning('Update "%s" caused error "%s"', bot, update.error)

# Функция которая соединяется с платформой telegram
def main():
    updater = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('bot start')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) #Когда придет команда start выполнится функция
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()













