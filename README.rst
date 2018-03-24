Le
==

.. image:: https://travis-ci.org/cganterh/le.svg?branch=master
.. image:: https://raw.githubusercontent.com/cganterh/le/master/coverage.svg?sanitize=true

Le is a silly extensible chatbot. This package is designed to load plugins in the entry point
groups ``le.parsers``, ``le.handlers`` and ``le.handlers.chat``.

For more examples on how to write new plugins you can look at the ones I wrote:

*	`lecluvindex <https://github.com/cganterh/lecluvindex>`_
*	`lehello <https://github.com/cganterh/lehello>`_
*	`lechat <https://github.com/cganterh/lechat>`_
*	`lemaster <https://github.com/cganterh/lemaster>`_

You can install any of these packages together and the run ``lebot`` to start your bot::

    lebot <telegram_token>

The usage of the command is::

	usage: lebot [-h] [-d] telegram_token

	positional arguments:
	  telegram_token

	optional arguments:
	  -h, --help      show this help message and exit
	  -d, --debug
