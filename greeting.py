import logging
from keyboard import main_keyboard

# Функция greet_user будет вызаваться, когда пользователь напишет /start или подключится к боту в первый раз
#Параметря принято называть bot & update (должно быть как минимум 2 параметра)
def greet_user(bot, update):
    #text = '''Hello, you can rule some command and get answer, like distance from Earth and
    #selectes planet on a input date: /Moon, /Mars, /Jupiter, /Saturn, /Venus, /Mercury, /Uranus '''
    text = '''Привет, ты можешь набрать команду состоящую из названия планеты и через пробел
      год в котором ты хочешь получить расстояние между Землёй и заданным небесным телом. 
      Названия планет: Mars, Jupiter, Saturn, Venus, Mercury, Uranus, Moon. . Команда выполняется 
      в виде: /planet Mars 1981. По команде /calc доступны арифметические действия над двумя 
      числами. Пример команды /calc 25 + 35
      '''
    print(text)
    logging.info(text)
    update.message.reply_text(text, reply_markup=main_keyboard())
