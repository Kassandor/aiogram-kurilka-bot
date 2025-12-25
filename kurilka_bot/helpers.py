import asyncio
from datetime import datetime, UTC, timedelta

from aiogram import Bot
from aiogram.types import Message

from kurilka_bot.settings import settings


class BotHelper:
    """
    Хелпер для бота
    """

    _last_poll_time: dict[int, datetime] = {}
    _poll_cooldown = settings.POLL_SMOKE_COLDOWN_MINUTES
    _lock = asyncio.Lock()

    @classmethod
    async def get_poll_cooldown(cls, chat_id: int) -> timedelta | None:
        last_poll_time = cls._last_poll_time.get(chat_id)

        if not last_poll_time:
            return None

        now = datetime.now(UTC)
        elapsed = now - last_poll_time
        if elapsed >= cls._poll_cooldown:
            return None

        return cls._poll_cooldown - elapsed

    @classmethod
    async def send_poll(cls, bot: Bot, message: Message) -> None:
        """
        Стартует голосование на покур
        :param bot: Бот
        :param message: Сообщение
        :return: None
        """

        chat_id = message.chat.id
        async with cls._lock:
            cooldown = await cls.get_poll_cooldown(chat_id)
            if cooldown:
                cooldown_minutes = cooldown.total_seconds() // 60
                previous_smoke_time = cls._last_poll_time.get(chat_id).strftime("%H:%M")

                await message.answer(
                    f'Уважаемый {message.from_user.full_name}! Перекур был в {previous_smoke_time}.'
                    f'Следующий перекур только через {max(1, int(cooldown_minutes))}'
                )
                return

            await bot.send_poll(
                chat_id=message.chat.id,
                question=f"Предложение от {message.from_user.full_name}: Пойдём курить? 🚬",
                options=["Да", "Нет"],
                is_anonymous=False,  # Голоса неанонимные
                allows_multiple_answers=False,
            )
            cls._last_poll_time[chat_id] = datetime.now(UTC)
