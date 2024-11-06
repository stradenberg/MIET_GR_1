import telebot
from telebot import types
import json


data = {
    "pon": {
        "id": "274576554589654"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

for x in range(1):
    a = random.randint(1, 45327457655458965435)
    print(a)
    data['id'] = a

print(data)


API_token = "7229027068:AAG4GRW-osArxEMs1rl7hWufpNBJmTpHk3U"

bot = telebot.TeleBot(API_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! МЕГА ВАЖНО", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'напиши задачу', reply_markup=markup)
    if message.text:
        print(message.text)


bot.infinity_polling()
