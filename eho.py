import logging

# эхобот ---отправляет пользователю тот текст который он написал
def talk_to_me(bot, update):

    text = 'Привет {}, ты написал {}.'.format(update.message.chat.username, update.message.text)
    update.message.reply_text(text)
    print(update.message)

    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                   update.message.chat.id, update.message.text)
