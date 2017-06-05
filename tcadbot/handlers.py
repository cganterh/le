from datetime import time
from difflib import get_close_matches
from logging import getLogger
# from pprint import pprint
from random import choice, random

import requests
from telegram.ext.jobqueue import Days


rooms = {}
logger = getLogger()


def hello(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text="Hi all, I'm the TCAD bot. More features comming soon."
    )


def objection(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text="Objection!"
    )


def print_uv_index(bot, chat_id):
    response = requests.get(
        'http://archivos.meteochile.gob.cl/portaldmc/meteochile/js/'
        'indice_radiacion.json'
    )

    data = response.json()
    radiation_data = data['RadiacionUVB']

    radiation_stgo = next(
        filter(lambda p: p['nombre'] == 'SANTIAGO', radiation_data)
    )

    date = radiation_stgo['fechapron']
    index = radiation_stgo['indicepron'].split(':')

    text = 'Pronostico Dia: {}. UV index: {}({})'.format(
        date, index[0], index[1])

    bot.sendMessage(
        chat_id=chat_id, text=text)


def get_uv_index(bot, update):
    print_uv_index(bot, update.message.chat_id)


def callback_uv_index(bot, job):
    print_uv_index(bot, job.context)


def start_uv_index(bot, update, job_queue, args):
    try:
        hour = int(args[0])
        minute = int(args[1])

        job_queue.run_daily(
            callback_uv_index,
            time=time(hour, minute),
            days=(Days.MON, Days.TUE, Days.WED, Days.THU, Days.FRI),
            context=update.message.chat_id,
            name='UV Index Daily Report'
        )

        bot.sendMessage(
            chat_id=update.message.chat_id,
            text='Initiating UV Index daily report.'
        )

    except IndexError:
        if len(args) is not 2:
            bot.sendMessage(
                chat_id=update.message.chat_id,
                text='You have to pass the hour and minute!'
            )

        else:
            bot.sendMessage(
                chat_id=update.message.chat_id, text='Something went wrong!')

    except:
        bot.sendMessage(
            chat_id=update.message.chat_id, text='Something went wrong!')


def stop_uv_index(bot, update, job_queue):
    for j in job_queue.jobs():
        if j.name == 'UV Index Daily Report' and \
                j.context == update.message.chat_id:
            j.schedule_removal()

    bot.sendMessage(
        chat_id=update.message.chat_id,
        text='Canceled all UV Index daily reports'
    )


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
    #
    # pprint(rooms)
    # print('---------------------------')
