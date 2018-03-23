Le
==

![Coverage badge](coverage.svg)

Le is a silly extensible chatbot. This package is designed to load plugins in the entry point
groups `le.parsers`, `le.handlers` and `le.handlers.chat`.

For more examples on how to write new plugins you can look at the ones I wrote:

*	[lecluvindex](https://github.com/cganterh/lecluvindex)
*	[lehello](https://github.com/cganterh/lehello)
*	[lechat](https://github.com/cganterh/lechat)
*	[lemaster](https://github.com/cganterh/lemaster)

You can install any of these packages together and the run lechat to start your bot:

    lebot <telegram_token>

The usage of the command is:

	usage: lebot [-h] [-d] telegram_token

	positional arguments:
	  telegram_token

	optional arguments:
	  -h, --help      show this help message and exit
	  -d, --debug
