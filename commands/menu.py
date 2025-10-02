from aiogram import types
from aiogram.filters import Command
from .base import BaseCommand

class MenuCommand(BaseCommand):
    """Menu command handler."""
    
    def register(self) -> None:
        """Register the menu command handler."""
        self.dp.message.register(self.menu_command, Command("menu"))
    
    async def menu_command(self, message: types.Message) -> None:
        """Handle the /menu command."""
        await message.answer("📋 Main Menu:", reply_markup=self._get_main_menu())
    
    def _get_main_menu(self):
        """Get the main menu keyboard."""
        from aiogram.utils.keyboard import InlineKeyboardBuilder
        
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="💰 Add Income/Expense", callback_data="add_transaction"))
        builder.add(types.InlineKeyboardButton(text="🎯 Set Savings Goal", callback_data="set_savings_goal"))
        builder.add(types.InlineKeyboardButton(text="📊 Financial Reports", callback_data="financial_reports"))
        builder.add(types.InlineKeyboardButton(text="🤖 Chat with AI Assistant", callback_data="ai_chat"))
        builder.adjust(2)  # Arrange buttons in 2 columns
        return builder.as_markup()
