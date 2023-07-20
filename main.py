import telebot
from data import character_pages
from telebot import types
import os
from os.path import join, dirname
from dotenv import load_dotenv
def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)
token = get_from_env('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    tip = types.KeyboardButton('Tip the author')
    help = types.KeyboardButton('View all list of memes(long list of 1000+)')
    markup.add(tip,help)
    bot.send_message(message.chat.id, "Enter keyword to generate meme", reply_markup=markup)
@bot.message_handler()
def echo_all(message):
    if message.text == 'Tip the author':
        bot.send_message(message.chat.id, 'https://www.buymeacoffee.com//wolfhoundt6')
    elif message.text == 'View all list of memes(long list of 1000+)':

        string_version = "\n".join(character_pages)
        if len(string_version) > 4096:
            for x in range(0, len(string_version), 4096):
                bot.send_message(message.chat.id, string_version[x:x + 4096])
            else:
                bot.send_message(message.chat.id, string_version)
    for element in character_pages:
        if message.text.lower() in element.lower():
            markup = types.InlineKeyboardMarkup()
            markup2 = types.InlineKeyboardButton(f"Choose this! {element}", callback_data=f"{element}")
            markup.add(markup2)
            element_to_send = element.replace(" ", "-")
            try:
                bot.send_photo(message.chat.id, f"http://apimeme.com/meme?meme={element_to_send}&top=Top+text&bottom=Bottom+text", reply_markup=markup)
            except:
                print (f"http://apimeme.com/meme?meme={element_to_send}&top=Top+text&bottom=Bottom+text")
@bot.callback_query_handler(func=lambda call: True)
def test_callback(call): # <- passes a CallbackQuery type object to your function
    user_info = {}
    user_info['meme'] = call.data.replace(" ", "-")
    msg = bot.send_message(call.message.chat.id, "Enter top text")
    bot.register_next_step_handler(msg, text_top_meme, user_info)
def text_top_meme(message, user_info):
    user_info['toptext'] = message.text.replace(" ", "+")
    msg = bot.send_message(message.chat.id, "Enter bottom text")
    bot.register_next_step_handler(msg, text_bot_meme, user_info)
    print('test112')
def text_bot_meme(message, user_info):
    user_info['bottext'] = message.text.replace(" ", "+")
    meme = user_info['meme']
    toptext = user_info['toptext']
    bottext = user_info['bottext']
    bot.send_photo(message.chat.id, f"http://apimeme.com/meme?meme={meme}&top={toptext}&bottom={bottext}")
    send_welcome(message)

bot.infinity_polling()