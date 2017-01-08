from difflib import get_close_matches
from logging import getLogger
from pprint import pprint
from random import choice, random

import requests


rooms = {}
logger = getLogger()


def hello(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text="Hi all, I'm the TCAD bot. More features comming soon."
    )


def get_uv_index(bot, update):
    response = requests.get(
        'http://archivos.meteochile.gob.cl/portaldmc/meteochile/js/'
        'indice_radiacion.json'
    )

    data = response.json()
    radiation_data = data['RadiacionUVB']

    radiation_stgo = next(
        filter(lambda p: p['nombre'] == 'SANTIAGO', radiation_data)
    )

    bot.sendMessage(
        chat_id=update.message.chat_id, text=radiation_stgo['indiceobs'])


def parse_normal_message(bot, update):
    cur_message = update.message.text
    chat_id = update.message.chat_id
    user = update.message.from_user.id

    if chat_id not in rooms:
        rooms[chat_id] = {
            'dict': {},
            'last_message': '',
            'last_user': None,
        }

    d = rooms[chat_id]['dict']
    last_message = rooms[chat_id]['last_message']
    last_user = rooms[chat_id]['last_user']

    if cur_message and last_message and last_user != user:
        d[last_message] = cur_message

    rooms[chat_id]['last_message'] = cur_message if cur_message else ''
    rooms[chat_id]['last_user'] = user

    previous_messages = d.keys()
    similar_messages = get_close_matches(cur_message, previous_messages)

    if len(similar_messages) > 0 and random() > 0.5:
        choosen_message = choice(similar_messages)
        response = d[choosen_message]
        bot.sendMessage(chat_id=update.message.chat_id, text=response)
        rooms[chat_id]['last_message'] = response

    pprint(rooms)
    print('---------------------------')
