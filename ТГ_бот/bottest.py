import sqlite3
import telebot
from telebot import types
import datetime

token = '5905459743:AAG7HVZqDa6evmM2p0il9KVLtozabh0Ro8w'
bot = telebot.TeleBot(token)


# conn = sqlite3.connect('tgdb.db', check_same_thread=False)
# cursor = conn.cursor()


# def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
#  cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
#  conn.commit()

# def get_info_about_users():
#  user_info = cursor.execute('SELECT * FROM test')
#  array = []
#  for user in user_info:
#   array.append(user[3])
#  return array


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
        # btn1 = types.KeyboardButton('Добавить информацию о себе')
        # btn2 = types.KeyboardButton('Информация')
        btn4 = types.KeyboardButton('Очень важно')
        markup.add(btn4)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup)
    elif message.text == 'Добавить информацию о себе':
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
        bot.send_message(message.chat.id, 'Ваше имя добавлено в базу данных!')
    elif message.text == 'Информация':
        information = get_info_about_users()
        bot.send_message(message.chat.id, "".join(str(information)))
    elif message.text == 'Какой сегодня день?':
        day = datetime.datetime.today().weekday()  # вернет день в формате от 0 до 6 (включительно)
        day_string = ''
        match day:
            case 0:
                day_string = 'Понедельник'
            case 1:
                day_string = 'Вторник'
        bot.send_message(message.chat.id, day_string)
    elif message.text == 'Очень важно':
        audio = open(r'/home/sergey/Documents/programming/tg_bots/giper_vazhno.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)


bot.polling(none_stop=True, interval=0)


def log(message):
    print("<!------!>")
    print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))