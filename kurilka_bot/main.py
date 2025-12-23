import asyncio
import logging
import sys

from aiogram import Dispatcher

from kurilka_bot.api.cmd import router as cmd_router
from kurilka_bot.api.controllers import router as controller_router
from kurilka_bot.bot import smoke_bot

dp = Dispatcher()
dp.include_router(cmd_router)
dp.include_router(controller_router)


async def main() -> None:
    await dp.start_polling(smoke_bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
