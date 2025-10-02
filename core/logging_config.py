"""
Centralized logging configuration for the financial planner bot.
Provides separate log files for different components with proper formatting.
"""

import logging
import logging.handlers
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from .config import config


class LoggingConfig:
    """Centralized logging configuration manager."""
    
    def __init__(self):
        self.log_dir = Path(config.LOG_DIR)
        self.log_dir.mkdir(exist_ok=True)
        
        # Log levels
        log_level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        self.log_level = log_level_map.get(config.LOG_LEVEL, logging.INFO)
        
        # Configure different loggers
        self._setup_loggers()
    
    def _setup_loggers(self):
        """Set up all loggers with appropriate handlers."""
        
        # Root logger configuration
        root_logger = logging.getLogger()
        root_logger.setLevel(self.log_level)
        
        # Clear any existing handlers
        root_logger.handlers.clear()
        
        # Bot logger
        self._setup_bot_logger()
        
        # Database logger
        self._setup_database_logger()
        
        # Session logger
        self._setup_session_logger()
        
        # General application logger
        self._setup_app_logger()
        
        # Error logger (catches all errors)
        self._setup_error_logger()
    
    def _setup_bot_logger(self):
        """Set up bot-specific logging."""
        bot_logger = logging.getLogger("bot")
        bot_logger.setLevel(self.log_level)
        
        # Bot log file handler
        bot_handler = logging.handlers.RotatingFileHandler(
            self.log_dir / "bot.log",
            maxBytes=config.LOG_MAX_SIZE,
            backupCount=config.LOG_BACKUP_COUNT,
            encoding='utf-8'
        )
        
        # Bot console handler (only in debug mode)
        if config.is_debug_mode():
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_formatter = logging.Formatter(
                '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            console_handler.setFormatter(console_formatter)
            bot_logger.addHandler(console_handler)
        
        # Bot file formatter
        bot_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        bot_handler.setFormatter(bot_formatter)
        bot_logger.addHandler(bot_handler)
        
        # Prevent propagation to root logger
        bot_logger.propagate = False
    
    def _setup_database_logger(self):
        """Set up database-specific logging."""
        db_logger = logging.getLogger("database")
        db_logger.setLevel(self.log_level)
        
        # Database log file handler
        db_handler = logging.handlers.RotatingFileHandler(
            self.log_dir / "database.log",
            maxBytes=config.LOG_MAX_SIZE,
            backupCount=config.LOG_BACKUP_COUNT,
            encoding='utf-8'
        )
        
        # Database formatter
        db_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(module)s:%(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        db_handler.setFormatter(db_formatter)
        db_logger.addHandler(db_handler)
        
        # Prevent propagation to root logger
        db_logger.propagate = False
    
    def _setup_session_logger(self):
        """Set up session-specific logging."""
        session_logger = logging.getLogger("session")
        session_logger.setLevel(self.log_level)
        
        # Session log file handler
        session_handler = logging.handlers.RotatingFileHandler(
            self.log_dir / "session.log",
            maxBytes=config.LOG_MAX_SIZE,
            backupCount=config.LOG_BACKUP_COUNT,
            encoding='utf-8'
        )
        
        # Session formatter
        session_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        session_handler.setFormatter(session_formatter)
        session_logger.addHandler(session_handler)
        
        # Prevent propagation to root logger
        session_logger.propagate = False
    
    def _setup_app_logger(self):
        """Set up general application logging."""
        app_logger = logging.getLogger("app")
        app_logger.setLevel(self.log_level)
        
        # App log file handler
        app_handler = logging.handlers.RotatingFileHandler(
            self.log_dir / "app.log",
            maxBytes=config.LOG_MAX_SIZE,
            backupCount=config.LOG_BACKUP_COUNT,
            encoding='utf-8'
        )
        
        # App formatter
        app_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(module)s:%(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        app_handler.setFormatter(app_formatter)
        app_logger.addHandler(app_handler)
        
        # Prevent propagation to root logger
        app_logger.propagate = False
    
    def _setup_error_logger(self):
        """Set up error-specific logging (catches all errors)."""
        error_logger = logging.getLogger("error")
        error_logger.setLevel(logging.ERROR)
        
        # Error log file handler
        error_handler = logging.handlers.RotatingFileHandler(
            self.log_dir / "error.log",
            maxBytes=config.LOG_MAX_SIZE,
            backupCount=config.LOG_BACKUP_COUNT,
            encoding='utf-8'
        )
        
        # Error formatter
        error_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(module)s:%(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        error_handler.setFormatter(error_formatter)
        error_logger.addHandler(error_handler)
        
        # Prevent propagation to root logger
        error_logger.propagate = False
    
    def get_logger(self, name: str) -> logging.Logger:
        """
        Get a logger instance for a specific component.
        
        Args:
            name (str): Logger name (bot, database, session, app, error)
            
        Returns:
            logging.Logger: Configured logger instance
        """
        return logging.getLogger(name)
    
    def log_startup_info(self):
        """Log startup information."""
        app_logger = self.get_logger("app")
        app_logger.info("=" * 60)
        app_logger.info(f"🚀 {config.BOT_NAME} Starting Up")
        app_logger.info(f"📝 Debug Mode: {'ON' if config.is_debug_mode() else 'OFF'}")
        app_logger.info(f"🔑 Token Status: {'✅ Set' if config.BOT_TOKEN else '❌ Missing'}")
        app_logger.info(f"🗄️ Database: {config.DB_NAME}@{config.DB_HOST}:{config.DB_PORT}")
        app_logger.info(f"⏰ Session Timeout: {config.SESSION_TIME} minutes")
        app_logger.info(f"📁 Log Directory: {self.log_dir.absolute()}")
        app_logger.info("=" * 60)


# Global logging configuration instance
logging_config = LoggingConfig()


def get_logger(name: str) -> logging.Logger:
    """
    Convenience function to get a logger instance.
    
    Args:
        name (str): Logger name (bot, database, session, app, error)
        
    Returns:
        logging.Logger: Configured logger instance
    """
    return logging_config.get_logger(name)


def setup_logging():
    """Initialize the logging system."""
    logging_config.log_startup_info()
    return logging_config
