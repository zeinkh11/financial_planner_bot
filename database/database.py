import asyncio
from typing import AsyncGenerator, Optional
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData, text

from core.config import config
from core.logging_config import get_logger

# Get database logger
logger = get_logger("database")


class Base(DeclarativeBase):
    """Base class for all database models."""

    metadata = MetaData()


class DatabaseManager:
    """Manages database connections and sessions."""

    def __init__(self):
        self.engine = None
        self.session_factory = None
        self._initialized = False

    async def initialize(self) -> None:
        """Initialize the database connection."""
        if self._initialized:
            return

        try:
            # Create async engine
            database_url = config.get_database_url()
            self.engine = create_async_engine(
                database_url,
                echo=config.is_debug_mode(),
                pool_pre_ping=True,
                pool_recycle=3600,
                pool_size=10,
                max_overflow=20,
            )

            # Create session factory
            self.session_factory = async_sessionmaker(
                self.engine, class_=AsyncSession, expire_on_commit=False
            )

            self._initialized = True
            logger.info("✅ Database connection initialized successfully")

        except Exception as e:
            logger.error(f"❌ Failed to initialize database connection: {e}")
            raise

    async def close(self) -> None:
        """Close the database connection."""
        if self.engine:
            await self.engine.dispose()
            self._initialized = False
            logger.info("🔒 Database connection closed")

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Get a database session."""
        if not self._initialized:
            await self.initialize()

        async with self.session_factory() as session:
            try:
                yield session
            except Exception as e:
                await session.rollback()
                logger.error(f"❌ Database session error: {e}")
                raise
            finally:
                await session.close()

    async def test_connection(self) -> bool:
        """Test the database connection."""
        try:
            async for session in self.get_session():
                await session.execute(text("SELECT 1"))
                logger.info("✅ Database connection test successful")
                return True
        except Exception as e:
            logger.error(f"❌ Database connection test failed: {e}")
            return False


# Global database manager instance
db_manager = DatabaseManager()


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get database session."""
    async for session in db_manager.get_session():
        yield session


async def init_database() -> None:
    """Initialize the database connection."""
    await db_manager.initialize()


async def close_database() -> None:
    """Close the database connection."""
    await db_manager.close()


async def test_database_connection() -> bool:
    """Test the database connection."""
    return await db_manager.test_connection()
