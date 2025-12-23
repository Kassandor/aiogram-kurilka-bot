from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from kurilka_bot.bot import smoke_bot
from kurilka_bot.helpers import BotHelper

router = Router()


@router.message(Command('vote1'))
async def cmd_vote1(message: Message) -> None:
    """
    Запуск голосования от имени бота через /vote1
    :param message: Сообщение
    :return: None
    """
    await BotHelper.send_poll(smoke_bot, message)
