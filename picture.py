import glob
from random import choice

def rockets(bot, update, context):

    rock_img_list = glob.glob('image/ro*.jp*')
    rock_img_filename = choice(rock_img_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(rock_img_filename, "rb"))
