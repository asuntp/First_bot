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
