"""
Session timeout handler for managing expired sessions and notifying users.
"""

import asyncio
from typing import List
from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.services.session_service import SessionService
from database.services.user_service import UserService
from core.config import config
from core.logging_config import get_logger

# Get session logger
logger = get_logger("session")


class SessionTimeoutHandler:
    """Handler for managing session timeouts and notifications."""

    def __init__(self, bot: Bot):
        """
        Initialize the session timeout handler.

        Args:
            bot (Bot): Aiogram bot instance for sending messages
        """
        self.bot = bot
        self.is_running = False

    async def start_timeout_checker(self) -> None:
        """Start the background task to check for expired sessions."""
        if self.is_running:
            return

        self.is_running = True
        logger.info("🔄 Session timeout checker started")

        while self.is_running:
            try:
                await self.check_and_handle_expired_sessions()
                # Check every 5 minutes
                await asyncio.sleep(60)
            except Exception as e:
                logger.error(f"❌ Error in session timeout checker: {e}")
                await asyncio.sleep(60)  # Wait 1 minute before retrying

    async def stop_timeout_checker(self) -> None:
        """Stop the background timeout checker."""
        self.is_running = False
        logger.info("🛑 Session timeout checker stopped")

    async def check_and_handle_expired_sessions(self) -> None:
        """Check for expired sessions and notify users."""
        try:
            # Get all expired sessions
            expired_sessions = await SessionService.get_expired_sessions()

            if not expired_sessions:
                return

            logger.info(f"🔍 Found {len(expired_sessions)} expired sessions")

            for session in expired_sessions:
                try:
                    # Get user information
                    user = await UserService.get_user_by_id(session.user_id)
                    if not user:
                        continue

                    # End the session
                    session_end_time = await SessionService.end_session(session.id)

                    if session_end_time:

                        # Send timeout notification to user
                        await self.send_session_timeout_message(
                            user.telegram_id, session, session_end_time
                        )

                        logger.info(
                            f"✅ Session {session.id} ended and user {user.telegram_id} notified"
                        )

                except Exception as e:
                    logger.error(f"❌ Error handling session {session.id}: {e}")
                    continue

        except Exception as e:
            logger.error(f"❌ Error checking expired sessions: {e}")

    async def send_session_timeout_message(
        self,
        telegram_id: int,
        session,
        session_end_time,
    ) -> None:
        """
        Send session timeout notification to user.

        Args:
            telegram_id (int): User's Telegram ID
            session: The expired session object
        """
        try:
            timeout_minutes = config.get_session_timeout()

            message_text = f"""
⏰ Session Timeout

Your AI Assistant session has expired after {timeout_minutes} minutes of inactivity.

Session Details:
• Session ID: {session.id}
• Started: {session.started_at.strftime('%Y-%m-%d %H:%M:%S')}
• Ended: {session_end_time.strftime('%Y-%m-%d %H:%M:%S')}

To start a new session, click the button below or use /start command.
            """

            # Create keyboard with "Start New Session" button
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="🤖 Start New Session", callback_data="ai_chat"
                        )
                    ]
                ]
            )

            await self.bot.send_message(
                chat_id=telegram_id, text=message_text, reply_markup=keyboard
            )

        except Exception as e:
            logger.error(f"❌ Error sending timeout message to user {telegram_id}: {e}")

    async def check_user_session_timeout(self, telegram_id: int) -> bool:
        """
        Check if a specific user's session has expired.

        Args:
            telegram_id (int): User's Telegram ID

        Returns:
            bool: True if session expired, False otherwise
        """
        try:
            # Get user
            user = await UserService.get_user_by_telegram_id(telegram_id)
            if not user:
                return False

            # Get active session
            active_session = await SessionService.get_active_session(user.id)
            if not active_session:
                return False

            # Check if session is expired
            is_expired = await SessionService.is_session_expired(active_session.id)

            if is_expired:
                # End the session and notify user
                session_end_time = await SessionService.end_session(active_session.id)
                if session_end_time:
                    await self.send_session_timeout_message(telegram_id, active_session, session_end_time)
                return True

            return False

        except Exception as e:
            logger.error(
                f"❌ Error checking session timeout for user {telegram_id}: {e}"
            )
            return False
