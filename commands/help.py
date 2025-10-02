from aiogram import types
from aiogram.filters import Command
from .base import BaseCommand
from core.config import config

class HelpCommand(BaseCommand):
    """Help command handler."""
    
    def register(self) -> None:
        """Register the help command handler."""
        self.dp.message.register(self.help_command, Command("help"))
    
    async def help_command(self, message: types.Message) -> None:
        """Handle the /help command."""
        help_text = f"""
🤖 {config.BOT_NAME} - Help

Available commands:
/start - Start the bot and show main menu
/menu - Show the main menu
/help - Show this help message

Main Features:
💰 Budget Planning
📊 Investment Analysis  
💳 Expense Tracking
📈 Financial Reports

For support, contact the bot administrator.
        """
        await message.answer(help_text)
