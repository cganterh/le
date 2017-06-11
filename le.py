"""Load and run all available handlers."""

import logging
from argparse import ArgumentParser

from pkg_resources import iter_entry_points
from telegram.ext import Updater


def run():
    """Run all handlers in the group ``le.handlers``."""
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    parser = ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument('telegram_token')
    args = parser.parse_args()

    updater = Updater(token=args.telegram_token)

    entry_points_iterator = iter_entry_points('le.handlers')
    handlers = (ep.load() for ep in entry_points_iterator)

    for handler in handlers:
        updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()
