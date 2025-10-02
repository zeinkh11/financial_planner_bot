import os
from dotenv import load_dotenv
from typing import Optional


class Config:
    """Configuration class to handle environment variables and bot settings."""

    def __init__(self, env_file: str = "config.env"):
        """
        Initialize configuration by loading environment variables.

        Args:
            env_file (str): Path to the environment file. Defaults to 'config.env'.
        """
        # Load environment variables from the specified file
        load_dotenv(env_file)

        # Bot configuration
        self.BOT_TOKEN: Optional[str] = os.getenv("BOT_TOKEN")
        self.BOT_NAME: str = os.getenv("BOT_NAME", "Financial Planner Bot")
        self.BOT_DESCRIPTION: str = os.getenv(
            "BOT_DESCRIPTION", "A simple financial planner bot"
        )

        # Database configuration
        self.DB_HOST: str = os.getenv("DB_HOST", "localhost")
        self.DB_PORT: int = int(os.getenv("DB_PORT", "3306"))
        self.DB_NAME: str = os.getenv("DB_NAME", "financial_planner_bot")
        self.DB_USER: str = os.getenv("DB_USER", "root")
        self.DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
        self.DB_CHARSET: str = os.getenv("DB_CHARSET", "utf8mb4")

        # Session configuration
        self.SESSION_TIME: int = int(
            os.getenv("SESSION_TIME", "30")
        )  # Session timeout in minutes

        # Optional settings
        self.DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
        
        # Logging configuration
        self.LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
        self.LOG_DIR: str = os.getenv("LOG_DIR", "logs")
        self.LOG_MAX_SIZE: int = int(os.getenv("LOG_MAX_SIZE", "10485760"))  # 10MB in bytes
        self.LOG_BACKUP_COUNT: int = int(os.getenv("LOG_BACKUP_COUNT", "5"))

        # Validate required configuration
        self._validate_config()

    def _validate_config(self) -> None:
        """Validate that required configuration is present."""
        if not self.BOT_TOKEN:
            raise ValueError(
                "BOT_TOKEN is required but not found in config.env file. "
                "Please add your bot token to the config.env file."
            )
        if not self.DB_PASSWORD:
            raise ValueError(
                "DB_PASSWORD is required but not found in config.env file. "
                "Please add your MySQL password to the config.env file."
            )

    def get_bot_info(self) -> dict:
        """
        Get bot information as a dictionary.

        Returns:
            dict: Dictionary containing bot configuration information.
        """
        return {
            "token": self.BOT_TOKEN,
            "name": self.BOT_NAME,
            "description": self.BOT_DESCRIPTION,
            "debug": self.DEBUG,
        }

    def is_debug_mode(self) -> bool:
        """
        Check if debug mode is enabled.

        Returns:
            bool: True if debug mode is enabled, False otherwise.
        """
        return self.DEBUG

    def get_session_timeout(self) -> int:
        """
        Get the session timeout in minutes.

        Returns:
            int: Session timeout in minutes.
        """
        return self.SESSION_TIME

    def get_database_url(self) -> str:
        """
        Get the database URL for SQLAlchemy.

        Returns:
            str: Database URL in SQLAlchemy format.
        """
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?charset={self.DB_CHARSET}"


# Create a global config instance
config = Config()
