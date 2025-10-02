from abc import ABC, abstractmethod
from aiogram import Dispatcher
from typing import Any, Dict

class BaseCommand(ABC):
    """Base class for all bot commands."""
    
    def __init__(self, dp: Dispatcher):
        """
        Initialize the command with dispatcher.
        
        Args:
            dp (Dispatcher): Aiogram dispatcher instance
        """
        self.dp = dp
        self.register()
    
    @abstractmethod
    def register(self) -> None:
        """Register the command handler with the dispatcher."""
        pass
    
    def get_command_name(self) -> str:
        """
        Get the command name.
        
        Returns:
            str: Command name without the leading slash
        """
        return self.__class__.__name__.lower().replace('command', '')
    
    def get_description(self) -> str:
        """
        Get command description.
        
        Returns:
            str: Command description
        """
        return f"Execute {self.get_command_name()} command"
