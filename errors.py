import logging

def error(bot, update):
    logging.warning('Update "%s" caused error "%s"', bot, update.error)
