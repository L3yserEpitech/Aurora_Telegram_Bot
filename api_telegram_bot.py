import telebot
from telebot import types
from telebot.util import quick_markup
import sys
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import api_excel

telegram_api_key = "6600000609:AAG9M4oEnkTWSHrfVlqlRFi20TWas7q2sfc"
bot = telebot.TeleBot(telegram_api_key)

@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    chat_id = call.message.chat.id
    data = call.data
    user_id = call.from_user.id
    

    if data == 'start':
        start(chat_id, call.from_user.username)
    if data == 'inscription':
        user_inscription(chat_id)
    elif data == 'major':
        user_country(chat_id)
    elif data == 'minor':
        user_minor(chat_id)
    elif data == 'user_in_eu' or data == 'user_out_eu':
        user_pack(chat_id)


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    username = message.from_user.username
    markup = InlineKeyboardMarkup(row_width=2)
    bt_inscription = InlineKeyboardButton('Inscription', callback_data='inscription')
    bt_info = InlineKeyboardButton('Info Robot Aurora', url="https://www.auroratrading.fr")
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")

    markup.add(bt_inscription, bt_support, bt_info)
    bot.send_message(chat_id, f"*Hello {username}, on te souhaite la bienvenue dans le team Aurora !* 💎 \
                    \n\nInscription / conctater un support", reply_markup=markup, parse_mode="Markdown")


def user_inscription(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    bt_major = InlineKeyboardButton('J\'ai +18ans', callback_data='major')
    bt_minor = InlineKeyboardButton('J\'ai -18ans', callback_data='minor')
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")
    
    markup.add(bt_major, bt_minor, bt_support)
    
    bot.send_message(chat_id, f"*Bienvenue dans le precessus d'inscription Aurora 💎*\n\
    \nPour information, les robot Aurora Trading sont *100% automatisés*\
    \n(pas de signaux à prendre, les trades s'ouvrent et se ferment automatiquement) 🤖\n\
    \n‼️*Voici un questionnaire obligatoire :\n\n      Quelle âge as-tu ?*"
    , reply_markup=markup, parse_mode="Markdown")
    api_excel.impor("Jules")
    


def user_minor(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    bt_back = InlineKeyboardButton('Back', callback_data='start')
    
    markup.add(bt_back)
    
    bot.send_message(chat_id, f"*on accepte pas les mineurs malheureusement*"\
    , reply_markup=markup, parse_mode="Markdown")


def user_pack(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    bt_pack_start = InlineKeyboardButton('500 - 1000€', callback_data='pack_start')
    bt_pack_investissor = InlineKeyboardButton('+1000€', callback_data='pack_investissor')
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")
    
    markup.add(bt_pack_start, bt_pack_investissor, bt_support)
    
    bot.send_message(chat_id, f"*Question 3/..\n\n➡️ Combien es-tu prêt/e à investir chez nous ?*"\
    , reply_markup=markup, parse_mode="Markdown")


def user_country(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    bt_in_eu = InlineKeyboardButton('Europe', callback_data='user_in_eu')
    bt_out_eu = InlineKeyboardButton('Hors Europe', callback_data='user_out_eu')
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")
    
    markup.add(bt_in_eu, bt_out_eu, bt_support)

    bot.send_message(chat_id, f"*Question 2/..\n\nTon pays de résidence ? 🌏*"\
    , reply_markup=markup, parse_mode="Markdown")


def start(chat_id, username):

    markup = InlineKeyboardMarkup(row_width=2)
    bt_inscription = InlineKeyboardButton('Inscription', callback_data='inscription')
    bt_info = InlineKeyboardButton('Info Robot Aurora', url="https://www.auroratrading.fr")
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")

    markup.add(bt_inscription, bt_support, bt_info)
    bot.send_message(chat_id, f"*Hello {username}, on te souhaite la bienvenue dans le team Aurora !* 💎 \
                    \n\nInscription / conctater un support", reply_markup=markup, parse_mode="Markdown")
    
    

    

    






# Démarrage du bot
bot.polling()
