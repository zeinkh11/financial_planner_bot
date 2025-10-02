from aiogram import types
from aiogram.filters import Command
from .base import BaseCommand
from core.config import config
from database.services.user_service import UserService


class StartCommand(BaseCommand):
    """Start command handler."""

    def register(self) -> None:
        """Register the start command handler."""
        self.dp.message.register(self.start_command, Command("start"))

    async def start_command(self, message: types.Message) -> None:
        """Handle the /start command."""
        # Get or create user and check if they're new
        user, is_new_user = await UserService.get_or_create_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )

        # Different welcome messages for new vs returning users
        if is_new_user:
            welcome_text = f"🎉 Welcome to {config.BOT_NAME}!"
        else:
            welcome_text = f"👋 Welcome back to {config.BOT_NAME}!"

        await message.answer(welcome_text)
