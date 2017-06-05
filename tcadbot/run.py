
import json
import logging
from sys import argv

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from .handlers import \
    hello, objection, get_uv_index, start_uv_index, stop_uv_index, \
    parse_normal_message


def run():
    try:
        logger = logging.getLogger()

        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

        with open(argv[1]) as f:
            config = json.load(f)

        updater = Updater(token=config['telegram_token'])

        updater.dispatcher.add_handler(
            CommandHandler('hi', hello)
        )

        updater.dispatcher.add_handler(
            CommandHandler('uvindex', get_uv_index)
        )

        updater.dispatcher.add_handler(
            CommandHandler(
                'start_uvindex',
                start_uv_index,
                pass_args=True,
                pass_job_queue=True
            )
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

    except FileNotFoundError:
        logger.critical('The config file could not be found.')
        exit(1)

    except IndexError:
        if len(argv) <= 2:
            logger.critical(
                "It seems you didn't pass a config file. Please talk "
                "to the @BotFather, create a new bot and put the generated "
                'token in a JSON file: '
                '{"telegram_token": '
                '"967437817:ib6cw-besi6ei6rUCUTuyvcwo7bcrib6ui1"}. Finally '
                'you can pass this file as an argument to this program.'
            )
            exit(1)

        else:
            raise
