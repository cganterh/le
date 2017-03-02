#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from .handlers import hello, objection, get_uv_index, start_uv_index, stop_uv_index, parse_normal_message


with open('config.json') as f:
    config = json.load(f)

updater = Updater(token=config['telegram_token'])

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater.dispatcher.add_handler(
    CommandHandler('hi', hello)
)

updater.dispatcher.add_handler(
    CommandHandler('uvindex', get_uv_index)
)

updater.dispatcher.add_handler(
    CommandHandler('start_uvindex', start_uv_index, pass_job_queue=True)
)

updater.dispatcher.add_handler(
    CommandHandler('stop_uvindex', stop_uv_index, pass_job_queue=True)
)

updater.dispatcher.add_handler(
    CommandHandler('objection', objection)
)

updater.dispatcher.add_handler(
    MessageHandler(Filters.all, parse_normal_message)
)

updater.start_polling()
updater.idle()
