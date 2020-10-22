import ephem

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
