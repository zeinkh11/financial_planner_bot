import asyncio
from aiogram import Bot, Dispatcher

# Import configuration from core module
from core.config import config
from core.logging_config import setup_logging, get_logger

# Import database functions
from database import init_database, close_database, test_database_connection

# Import command handlers
from commands import register_handlers
from core.session_timeout import SessionTimeoutHandler

# Initialize logging
setup_logging()
logger = get_logger("bot")

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

# Initialize session timeout handler
session_timeout_handler = SessionTimeoutHandler(bot)

# Register all command handlers
register_handlers(dp)

# Main function to run the bot
async def main():
    try:
        # Log configuration information
        logger.info(f"🚀 Starting {config.BOT_NAME}...")
        
        # Initialize database connection
        logger.info("🔄 Initializing database connection...")
        await init_database()
        
        # Test database connection
        if await test_database_connection():
            logger.info("✅ Database connection established")
        else:
            logger.error("❌ Database connection failed")
            return
        
        # Start session timeout checker
        logger.info("🔄 Starting session timeout checker...")
        timeout_task = asyncio.create_task(session_timeout_handler.start_timeout_checker())
        
        # Start polling
        logger.info("🔄 Starting bot polling...")
        await dp.start_polling(bot)
        
    except ValueError as e:
        logger.error(f"❌ Configuration Error: {e}")
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}")
    finally:
        # Stop session timeout checker
        logger.info("🔄 Stopping session timeout checker...")
        await session_timeout_handler.stop_timeout_checker()
        
        # Close database connection
        logger.info("🔄 Closing database connection...")
        await close_database()
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
