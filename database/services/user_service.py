"""
User service for database operations related to users.
"""

from typing import Optional, List, Tuple
from sqlalchemy import select

from ..database import get_db_session
from ..models import User, Session


class UserService:
    """Service for user-related database operations."""

    @staticmethod
    async def get_or_create_user(
        telegram_id: int,
        username: str = None,
        first_name: str = None,
        last_name: str = None,
    ) -> Tuple[User, bool]:
        """
        Get existing user or create new one.
        
        Returns:
            Tuple[User, bool]: (user_object, is_newly_created)
            - user_object: The User instance
            - is_newly_created: True if user was just created, False if user already existed
        """
        async for session in get_db_session():
            # Try to get existing user
            result = await session.execute(
                select(User).where(User.telegram_id == telegram_id)
            )
            user = result.scalar_one_or_none()

            if user:
                # Update user info if provided
                if username is not None:
                    user.username = username
                if first_name is not None:
                    user.first_name = first_name
                if last_name is not None:
                    user.last_name = last_name
                await session.commit()
                return user, False  # User already existed
            else:
                # Create new user
                user = User(
                    telegram_id=telegram_id,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                )
                session.add(user)
                await session.commit()
                await session.refresh(user)
                return user, True  # User was newly created

    @staticmethod
    async def get_user_by_id(user_id: int) -> Optional[User]:
        """Get user by internal ID."""
        async for session in get_db_session():
            result = await session.execute(select(User).where(User.id == user_id))
            return result.scalar_one_or_none()
            
    # @staticmethod
    # async def get_user_by_telegram_id(telegram_id: int) -> Optional[User]:
    #     """Get user by Telegram ID."""
    #     async for session in get_db_session():
    #         result = await session.execute(
    #             select(User).where(User.telegram_id == telegram_id)
    #         )
    #         return result.scalar_one_or_none()


    # @staticmethod
    # async def get_user_sessions(user_id: int) -> List[Session]:
    #     """Get all sessions for a user."""
    #     async for session in get_db_session():
    #         result = await session.execute(
    #             select(Session).where(Session.user_id == user_id)
    #         )
    #         return result.scalars().all()


    # @staticmethod
    # async def update_user_info(user_id: int, **kwargs) -> bool:
    #     """Update user information."""
    #     async for session in get_db_session():
    #         result = await session.execute(select(User).where(User.id == user_id))
    #         user = result.scalar_one_or_none()
    #         if user:
    #             for key, value in kwargs.items():
    #                 if hasattr(user, key):
    #                     setattr(user, key, value)
    #             await session.commit()
    #             return True
    #         return False

