from logging import getLogger


logger = getLogger()


def objection(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text="Objection!"
    )
