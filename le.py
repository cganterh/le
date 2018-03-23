"""Load and run all available handlers."""

import logging
from argparse import ArgumentParser

from typing import (    # noqa
    Generator,
    List,
)

from pkg_resources import (     # noqa
    EntryPoint,
    iter_entry_points,
)

from telegram.ext import Updater


def create_argument_parser() -> ArgumentParser:
    """Return a new argument parser."""
    entry_point_iterator = iter_entry_points(
        'le.parsers')   # type: Generator[EntryPoint, None, None]

    other_parsers = [
        ep.load()
        for ep in entry_point_iterator
    ]   # type: List[ArgumentParser]

    parser = ArgumentParser(
        parents=other_parsers, fromfile_prefix_chars='@')

    parser.add_argument('telegram_token')
    parser.add_argument('-d', '--debug', action='store_true')
    return parser


def run():
    """Run all handlers in the group ``le.handlers``."""
    args = create_argument_parser().parse_args()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG if args.debug else logging.INFO
    )

    logging.getLogger('telegram.ext').setLevel(logging.INFO)
    logging.getLogger('telegram.bot').setLevel(logging.INFO)
    logging.getLogger('telegram.vendor').setLevel(logging.INFO)

    updater = Updater(token=args.telegram_token)

    entry_points_iterator = iter_entry_points('le.handlers')
    handlers = ((ep.name, ep.load()) for ep in entry_points_iterator)

    for name, handler in handlers:
        updater.dispatcher.add_handler(handler)

        logging.getLogger().debug(
            'Loaded {}: {}'.format(name, handler)
        )

    entry_points_iterator = iter_entry_points('le.handlers.chat')
    chat_handlers = ((ep.name, ep.load()) for ep in entry_points_iterator)

    for group, (name, handler) in enumerate(chat_handlers, start=1):
        updater.dispatcher.add_handler(handler, group)

        logging.getLogger().debug(
            'Loaded {}: {}'.format(name, handler)
        )

    updater.start_polling()
    updater.idle()
