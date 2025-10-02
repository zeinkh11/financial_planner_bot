from aiogram import types
from .base import BaseCommand

class EchoHandler(BaseCommand):
    """Echo handler for unrecognized messages."""
    
    def register(self) -> None:
        """Register the echo handler."""
        self.dp.message.register(self.echo_handler)
    
    async def echo_handler(self, message: types.Message) -> None:
        """Handle unrecognized messages."""
        await message.answer(
            "I didn't understand that. Please use /menu to see available options or /help for more information."
        )
