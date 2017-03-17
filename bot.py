import time
import sys
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove

f = []
f.append(1368939191)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'contact':
        print(content_type, chat_type, chat_id, msg['contact']['phone_number'])
        markup = ReplyKeyboardRemove()
        bot.sendMessage(chat_id, msg['contact']['phone_number'], reply_markup=markup)
    else:
        print(content_type, chat_type, chat_id, msg['text'])
        if chat_id not in f:
            markup = ReplyKeyboardMarkup(keyboard=[
                [dict(text='Отправить номер телефона', request_contact=True)],
            ])
            bot.sendMessage(chat_id, 'Для авторизации в приложении отправьте, пожалуйста, ваш номер телефона.', reply_markup=markup)
            return

TOKEN = sys.argv[1] 

bot = telepot.Bot(TOKEN)

bot.message_loop(handle)
print('Listening ...')


while 1:
    time.sleep(100)