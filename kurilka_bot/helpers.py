from aiogram import Bot
from aiogram.types import Message


class BotHelper:
    """
    Хелпер для бота
    """

    @staticmethod
    async def send_poll(bot: Bot, message: Message) -> None:
        """
        Стартует голосование на покур
        :param bot: Бот
        :param message: Сообщение
        :return: None
        """
        await bot.send_poll(
            chat_id=message.chat.id,
            question=f"Предложение от {message.from_user.full_name}: Пойдём курить? 🚬",
            options=["Да", "Нет"],
            is_anonymous=False,  # Голоса неанонимные
            allows_multiple_answers=False,
        )
