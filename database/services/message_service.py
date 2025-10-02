"""
Message service for database operations related to messages.
"""

from typing import Optional, List
from sqlalchemy import select
from datetime import datetime, timedelta

from ..database import get_db_session
from ..models import Message


class MessageService:
    """Service for message-related database operations."""

    @staticmethod
    async def create_user_message(
        session_id: int,
        user_content: str,
        user_telegram_message_id: int = None,
    ) -> Message:
        """Create a new message record with user content (bot reply will be added later)."""
        async for session in get_db_session():
            message = Message(
                session_id=session_id,
                user_content=user_content,
                user_telegram_message_id=user_telegram_message_id,
            )
            session.add(message)
            await session.commit()
            await session.refresh(message)
            return message

    @staticmethod
    async def add_bot_reply(
        message_id: int,
        bot_content: str,
        bot_telegram_message_id: int = None,
        processing_time_ms: int = None,
    ) -> bool:
        """Add bot reply to an existing message record."""
        async for session in get_db_session():
            result = await session.execute(
                select(Message).where(Message.id == message_id)
            )
            message = result.scalar_one_or_none()
            if message:
                message.bot_content = bot_content
                message.bot_telegram_message_id = bot_telegram_message_id
                message.bot_sent_at = datetime.now()
                message.is_processed = True
                if processing_time_ms is not None:
                    message.processing_time_ms = processing_time_ms
                await session.commit()
                return True
            return False

    @staticmethod
    async def create_message_pair(
        session_id: int,
        user_content: str,
        bot_content: str = None,
        user_telegram_message_id: int = None,
        bot_telegram_message_id: int = None,
        processing_time_ms: int = None,
    ) -> Message:
        """Create a complete message pair (user message + bot reply) in one go."""
        async for session in get_db_session():
            message = Message(
                session_id=session_id,
                user_content=user_content,
                user_telegram_message_id=user_telegram_message_id,
                bot_content=bot_content,
                bot_telegram_message_id=bot_telegram_message_id,
                bot_sent_at=datetime.now() if bot_content else None,
                is_processed=bot_content is not None,
                processing_time_ms=processing_time_ms,
            )
            session.add(message)
            await session.commit()
            await session.refresh(message)
            return message

    @staticmethod
    async def get_session_messages(session_id: int, limit: int = 50) -> List[Message]:
        """Get messages for a session."""
        async for session in get_db_session():
            result = await session.execute(
                select(Message)
                .where(Message.session_id == session_id)
                .order_by(Message.user_sent_at.desc())
                .limit(limit)
            )
            return result.scalars().all()

    @staticmethod
    async def get_message_by_id(message_id: int) -> Optional[Message]:
        """Get message by ID."""
        async for session in get_db_session():
            result = await session.execute(
                select(Message).where(Message.id == message_id)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def get_unprocessed_messages(session_id: int = None) -> List[Message]:
        """Get messages that haven't been processed by the bot yet."""
        async for session in get_db_session():
            query = select(Message).where(Message.is_processed == False)
            if session_id:
                query = query.where(Message.session_id == session_id)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update_processing_time(message_id: int, processing_time_ms: int) -> bool:
        """Update the processing time for a message."""
        async for session in get_db_session():
            result = await session.execute(
                select(Message).where(Message.id == message_id)
            )
            message = result.scalar_one_or_none()
            if message:
                message.processing_time_ms = processing_time_ms
                await session.commit()
                return True
            return False

    @staticmethod
    async def get_messages_by_user_telegram_id(
        telegram_message_id: int,
    ) -> Optional[Message]:
        """Get message by user's Telegram message ID."""
        async for session in get_db_session():
            result = await session.execute(
                select(Message).where(
                    Message.user_telegram_message_id == telegram_message_id
                )
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def get_messages_by_bot_telegram_id(
        telegram_message_id: int,
    ) -> Optional[Message]:
        """Get message by bot's Telegram message ID."""
        async for session in get_db_session():
            result = await session.execute(
                select(Message).where(
                    Message.bot_telegram_message_id == telegram_message_id
                )
            )
            return result.scalar_one_or_none()


    @staticmethod
    async def get_recent_messages(session_id: int, hours: int = 24) -> List[Message]:
        """Get messages from the last N hours."""
        async for session in get_db_session():
            cutoff_time = datetime.now() - timedelta(hours=hours)
            result = await session.execute(
                select(Message)
                .where(
                    Message.session_id == session_id,
                    Message.user_sent_at >= cutoff_time,
                )
                .order_by(Message.user_sent_at.desc())
            )
            return result.scalars().all()
