"""
Command handlers registration module.
This module imports and registers all command handlers with the dispatcher.
"""

from aiogram import Dispatcher
from .start import StartCommand
from .menu import MenuCommand
from .help import HelpCommand
from .callbacks import CallbackHandlers
from .echo import EchoHandler
from core.logging_config import get_logger

# Get app logger
logger = get_logger("app")

def register_handlers(dp: Dispatcher) -> None:
    """
    Register all command handlers with the dispatcher.
    
    Args:
        dp (Dispatcher): Aiogram dispatcher instance
    """
    # Initialize all command handlers
    # They will automatically register themselves with the dispatcher
    StartCommand(dp)
    MenuCommand(dp)
    HelpCommand(dp)
    CallbackHandlers(dp)
    EchoHandler(dp)
    
    logger.info("✅ All command handlers registered successfully!")
