"""
Session service for database operations related to sessions.
"""

from typing import Optional, List
from sqlalchemy import select
from datetime import datetime, timedelta

from ..database import get_db_session
from ..models import Session
from core.config import config
from core.logging_config import get_logger

# Get database logger
logger = get_logger("database")


class SessionService:
    """Service for session-related database operations."""

    @staticmethod
    async def create_session(
        user_id: int,
        context_data: str = None,
    ) -> Session:
        """Create a new session."""
        async for session in get_db_session():
            session_obj = Session(
                user_id=user_id,
                context_data=context_data,
            )
            session.add(session_obj)
            await session.commit()
            await session.refresh(session_obj)
            return session_obj

    @staticmethod
    async def get_active_session(user_id: int) -> Optional[Session]:
        """Get the active session for a user."""
        async for session in get_db_session():
            result = await session.execute(
                select(Session)
                .where(Session.user_id == user_id, Session.is_active == True)
                .order_by(Session.last_activity.desc())
            )
            logger.debug(f"Query result for active session for user {user_id}: {result}")
            return result.scalar_one_or_none()

    @staticmethod
    async def is_session_expired(session_id: int) -> bool:
        """Check if a session has expired based on SESSION_TIME configuration."""
        async for session in get_db_session():
            result = await session.execute(
                select(Session).where(Session.id == session_id)
            )
            session_obj = result.scalar_one_or_none()
            if not session_obj:
                return True
            
            # Calculate if session has exceeded the timeout
            timeout_minutes = config.get_session_timeout()
            timeout_delta = timedelta(minutes=timeout_minutes)
            current_time = datetime.now()
            
            # Check if last activity + timeout is less than current time
            return (session_obj.last_activity + timeout_delta) < current_time

    @staticmethod
    async def get_expired_sessions() -> List[Session]:
        """Get all expired sessions that are still marked as active."""
        async for session in get_db_session():
            timeout_minutes = config.get_session_timeout()
            timeout_delta = timedelta(minutes=timeout_minutes)
            cutoff_time = datetime.now() - timeout_delta
            
            result = await session.execute(
                select(Session)
                .where(
                    Session.is_active == True,
                    Session.last_activity < cutoff_time
                )
            )
            return result.scalars().all()

    @staticmethod
    async def end_session(session_id: int) -> Optional[datetime]:
        """End a session by setting is_active to False."""
        async for session in get_db_session():
            result = await session.execute(
                select(Session).where(Session.id == session_id)
            )
            session_obj = result.scalar_one_or_none()
            if session_obj:
                session_end_time = datetime.now()
                session_obj.is_active = False
                session_obj.ended_at = session_end_time
                await session.commit()
                return session_end_time
            return None

    @staticmethod
    async def update_session_activity(session_id: int) -> bool:
        """Update session last activity timestamp."""
        async for session in get_db_session():
            result = await session.execute(
                select(Session).where(Session.id == session_id)
            )
            session_obj = result.scalar_one_or_none()
            if session_obj:
                session_obj.last_activity = datetime.now()
                await session.commit()
                return True
            return False

    # @staticmethod
    # async def get_active_session(user_id: int) -> Optional[Session]:
    #     """Get the active session for a user."""
    #     async for session in get_db_session():
    #         result = await session.execute(
    #             select(Session)
    #             .where(Session.user_id == user_id, Session.is_active == True)
    #             .order_by(Session.last_activity.desc())
    #         )
    #         return result.scalar_one_or_none()

    # @staticmethod
    # async def get_session_by_id(session_id: int) -> Optional[Session]:
    #     """Get session by ID."""
    #     async for session in get_db_session():
    #         result = await session.execute(
    #             select(Session).where(Session.id == session_id)
    #         )
    #         return result.scalar_one_or_none()

    # @staticmethod
    # async def end_session(session_id: int) -> bool:
    #     """End a session."""
    #     async for session in get_db_session():
    #         result = await session.execute(
    #             select(Session).where(Session.id == session_id)
    #         )
    #         session_obj = result.scalar_one_or_none()
    #         if session_obj:
    #             session_obj.is_active = False
    #             session_obj.ended_at = datetime.now()
    #             await session.commit()
    #             return True
    #         return False

    # @staticmethod
    # async def update_session_activity(session_id: int) -> bool:
    #     """Update session last activity timestamp."""
    #     async for session in get_db_session():
    #         result = await session.execute(
    #             select(Session).where(Session.id == session_id)
    #         )
    #         session_obj = result.scalar_one_or_none()
    #         if session_obj:
    #             session_obj.last_activity = datetime.now()
    #             await session.commit()
    #             return True
    #         return False

    # @staticmethod
    # async def update_session_context(session_id: int, context_data: str) -> bool:
    #     """Update session context data."""
    #     async for session in get_db_session():
    #         result = await session.execute(
    #             select(Session).where(Session.id == session_id)
    #         )
    #         session_obj = result.scalar_one_or_none()
    #         if session_obj:
    #             session_obj.context_data = context_data
    #             await session.commit()
    #             return True
    #         return False

    # @staticmethod
    # async def get_user_sessions(
    #     user_id: int, active_only: bool = False
    # ) -> list[Session]:
    #     """Get all sessions for a user."""
    #     async for session in get_db_session():
    #         query = select(Session).where(Session.user_id == user_id)
    #         if active_only:
    #             query = query.where(Session.is_active == True)
    #         query = query.order_by(Session.last_activity.desc())

    #         result = await session.execute(query)
    #         return result.scalars().all()

    # @staticmethod
    # async def reactivate_session(session_id: int) -> bool:
    #     """Reactivate a session."""
    #     async for session in get_db_session():
    #         result = await session.execute(
    #             select(Session).where(Session.id == session_id)
    #         )
    #         session_obj = result.scalar_one_or_none()
    #         if session_obj:
    #             session_obj.is_active = True
    #             session_obj.last_activity = datetime.now()
    #             await session.commit()
    #             return True
    #         return False
