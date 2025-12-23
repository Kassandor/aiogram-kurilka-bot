from aiogram import Router
from aiogram.types import Message

from kurilka_bot.bot import smoke_bot
from kurilka_bot.helpers import BotHelper

router = Router()


@router.message()
async def handle_bot_mention(message: Message) -> None:
    """
    Если бота упомянули в сообщении - стартует голосование
    :param message: Сообщение
    :return: None
    """
    bot_username = (await smoke_bot.me()).username.lower()
    mentioned = False
    for entity in message.entities:
        if entity.type == "mention":
            username = str(message.text)[entity.offset + 1 : entity.offset + entity.length].lower()
            if username == bot_username:
                mentioned = True
                break

    if not mentioned:
        return

    await BotHelper.send_poll(smoke_bot, message)
