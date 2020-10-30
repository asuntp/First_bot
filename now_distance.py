import ephem
import datetime
from keyboard import main_keyboard

def now(bot, update):

    try:
        year = '2020'


        distance1 = int(ephem.Mars(year).earth_distance) * 149597870
        user_text1 = 'В {} году расстояние между Землей и Марсом: {} k.m.'.format(year, distance1)

        distance2 = int(ephem.Moon(year).earth_distance) * 149597870
        user_text2 = 'В {} году расстояние между Землей и Луной: {} k.m.'.format(year, distance2)

        distance3 = int(ephem.Jupiter(year).earth_distance) * 149597870
        user_text3 = 'В {} году расстояние между Землей и Юпитером: {} k.m.'.format(year, distance3)

        distance4 = int(ephem.Saturn(year).earth_distance) * 149597870
        user_text4 = 'В {} году расстояние между Землей и Сатурном: {} k.m.'.format(year, distance4)

        distance5= int(ephem.Venus(year).earth_distance) * 149597870
        user_text5 = 'В {} году расстояние между Землей и Венерой: {} k.m.'.format(year, distance5)

        distance6 = int(ephem.Mercury(year).earth_distance) * 149597870
        user_text6 = 'В {} году расстояние между Землей и Меркурием: {} k.m.'.format(year, distance6)

        distance7 = int(ephem.Uranus(year).earth_distance) * 149597870
        user_text7 = 'В {} году расстояние между Землей и Ураном: {} k.m.'.format(year, distance7)
        user_text = user_text1 + user_text2 + user_text3 + user_text4 + user_text5 + user_text6 + user_text7
        update.message.reply_text(user_text, reply_markup=main_keyboard())

    except TypeError:
        update.message.reply_text("По команде /start вызываются правильные примеры команд")
