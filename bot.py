# coding=utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import time
import sys
import os
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove
from flask import Flask
import pyodbc
import logging

f = []
f.append(1368939191)
f.append(125969275)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'contact':
        print(content_type, chat_type, chat_id, msg['contact']['phone_number'])
        markup = ReplyKeyboardRemove()
        phone_number = msg['phone_number']
        bot.sendMessage(chat_id, msg['contact']['phone_number'], reply_markup=markup)
        contact_update(bot, chat_id, phone_number )
        logger.setLevel(logging.INFO)
    else:
        print(content_type, chat_type, chat_id, msg['text'])
        if chat_id not in f:
            markup = ReplyKeyboardMarkup(keyboard=[
                [dict(text='Отправить номер телефона', request_contact=True)],
            ])
            bot.sendMessage(chat_id, 'Для авторизации в приложении отправьте, пожалуйста, ваш номер телефона.', reply_markup=markup)
            return

def contact_update(bot, chat_id, phone_number)

    server = 'azure.database.windows.net'
    database = 'azuredatabase'
    username = 'azurerusername'
    password = 'azurepassword'

    driver= '{ODBC Driver 13 for SQL Server}'
    cnxn= pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("update contact set chat_id = chat_id from contact where phone_number=phone_number")
return


#TOKEN = sys.argv[1]
TOKEN = os.environ['TOKEN']
bot = telepot.Bot(TOKEN)



bot.message_loop(handle)
print('Listening ...')

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

while 1:
    time.sleep(100)
