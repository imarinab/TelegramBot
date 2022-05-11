import config
import telebot
import requests
from telebot import types

bot = telebot.TeleBot(config.token)
response = requests.get(config.url).json()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('USD')
    itembtn2 = types.KeyboardButton('EUR')
    itembtn3 = types.KeyboardButton('RUB')
    itembtn4 = types.KeyboardButton('PLN')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    msg = bot.send_message(message.chat.id, 'Choose currency', reply_markup=markup)
    bot.register_next_step_handler(msg, process_coin_step)

def process_coin_step(message):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)

        for coin in response:
            if (message.text == coin['Cur_Abbreviation']):
                bot.send_message(message.chat.id, printCoin(coin['Cur_Scale'], coin['Cur_OfficialRate']),
                                 reply_markup=markup, parse_mode='Markdown')

    except Exeption as e:
        bot.reply_to(message, 'try again')

def printCoin(Cur_Scale, Cur_OfficialRate):
    return "Currency rate: " + str(Cur_Scale) + "BYN = " + str(Cur_OfficialRate)
    bot.send_welcome(message)


bot.polling(none_stop=True)