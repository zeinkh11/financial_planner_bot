from aiogram import types
from .base import BaseCommand
from database.services.user_service import UserService
from database.services.session_service import SessionService
from core.config import config


class CallbackHandlers(BaseCommand):
    """Callback query handlers for inline buttons."""

    def register(self) -> None:
        """Register all callback handlers."""
        self.dp.callback_query.register(
            self.add_transaction_callback, lambda c: c.data == "add_transaction"
        )
        self.dp.callback_query.register(
            self.set_savings_goal_callback, lambda c: c.data == "set_savings_goal"
        )
        self.dp.callback_query.register(
            self.financial_reports_callback, lambda c: c.data == "financial_reports"
        )
        self.dp.callback_query.register(
            self.ai_chat_callback, lambda c: c.data == "ai_chat"
        )

    async def add_transaction_callback(
        self, callback_query: types.CallbackQuery
    ) -> None:
        """Handle add income/expense button callback."""
        await callback_query.answer()
        await callback_query.message.edit_text(
            "💰 Add Income/Expense\n\n"
            "This feature will help you:\n"
            "• Track your income sources\n"
            "• Log daily expenses\n"
            "• Categorize transactions\n"
            "• Monitor cash flow\n\n"
            "Feature coming soon! 🚀",
            reply_markup=self._get_main_menu(),
        )

    async def set_savings_goal_callback(
        self, callback_query: types.CallbackQuery
    ) -> None:
        """Handle set savings goal button callback."""
        await callback_query.answer()
        await callback_query.message.edit_text(
            "🎯 Set Savings Goal\n\n"
            "This feature will help you:\n"
            "• Define financial targets\n"
            "• Track progress towards goals\n"
            "• Set milestone reminders\n"
            "• Calculate required savings\n\n"
            "Feature coming soon! 🚀",
            reply_markup=self._get_main_menu(),
        )

    async def financial_reports_callback(
        self, callback_query: types.CallbackQuery
    ) -> None:
        """Handle financial reports button callback."""
        await callback_query.answer()
        await callback_query.message.edit_text(
            "📊 Financial Reports\n\n"
            "This feature will help you:\n"
            "• Monthly financial summaries\n"
            "• Spending trends analysis\n"
            "• Income vs expense charts\n"
            "• Goal progress tracking\n\n"
            "Feature coming soon! 🚀",
            reply_markup=self._get_main_menu(),
        )

    async def ai_chat_callback(self, callback_query: types.CallbackQuery) -> None:
        """Handle AI chat button callback - creates new session."""
        await callback_query.answer()

        try:
            # Get or create user first
            user, _ = await UserService.get_or_create_user(
                telegram_id=callback_query.from_user.id,
                username=callback_query.from_user.username,
                first_name=callback_query.from_user.first_name,
                last_name=callback_query.from_user.last_name,
            )

            # Check if user has an active session
            active_session = await SessionService.get_active_session(user.id)
            
            if active_session:
                # Check if the existing session is expired
                is_expired = await SessionService.is_session_expired(active_session.id)
                
                if is_expired:
                    # End expired session and create new one
                    await SessionService.end_session(active_session.id)
                    session = await SessionService.create_session(
                        user_id=user.id, context_data="AI Assistant Chat Session"
                    )
                    message_text = (
                        f"🤖 Chat with AI Assistant\n\n"
                        f"⏰ Your previous session expired after {config.get_session_timeout()} minutes of inactivity.\n"
                        f"✅ New session created successfully!\n"
                        f"Session ID: {session.id}\n"
                        f"Started at: {session.started_at.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                        f"I'm ready to help you with your financial questions and planning! "
                        f"Just send me a message and I'll assist you.\n\n"
                        f"Type /menu to return to the main menu anytime."
                    )
                else:
                    # Update session activity and continue existing session
                    await SessionService.update_session_activity(active_session.id)
                    message_text = (
                        f"🤖 Chat with AI Assistant\n\n"
                        f"✅ Continuing your existing session!\n"
                        f"Session ID: {active_session.id}\n"
                        f"Started at: {active_session.started_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"Last activity: {active_session.last_activity.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                        f"I'm ready to help you with your financial questions and planning! "
                        f"Just send me a message and I'll assist you.\n\n"
                        f"Type /menu to return to the main menu anytime."
                    )
            else:
                # Create new session
                session = await SessionService.create_session(
                    user_id=user.id, context_data="AI Assistant Chat Session"
                )
                message_text = (
                    f"🤖 Chat with AI Assistant\n\n"
                    f"✅ New session created successfully!\n"
                    f"Session ID: {session.id}\n"
                    f"Started at: {session.started_at.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                    f"I'm ready to help you with your financial questions and planning! "
                    f"Just send me a message and I'll assist you.\n\n"
                    f"Type /menu to return to the main menu anytime."
                )

            await callback_query.message.edit_text(message_text)

        except Exception as e:
            await callback_query.message.edit_text(
                f"❌ Error creating session: {str(e)}\n\n"
                f"Please try again later or contact support.",
                reply_markup=self._get_main_menu(),
            )

    def _get_main_menu(self):
        """Get the main menu keyboard."""
        from aiogram.utils.keyboard import InlineKeyboardBuilder

        builder = InlineKeyboardBuilder()
        builder.add(
            types.InlineKeyboardButton(
                text="💰 Add Income/Expense", callback_data="add_transaction"
            )
        )
        builder.add(
            types.InlineKeyboardButton(
                text="🎯 Set Savings Goal", callback_data="set_savings_goal"
            )
        )
        builder.add(
            types.InlineKeyboardButton(
                text="📊 Financial Reports", callback_data="financial_reports"
            )
        )
        builder.add(
            types.InlineKeyboardButton(
                text="🤖 Chat with AI Assistant", callback_data="ai_chat"
            )
        )
        builder.adjust(2)  # Arrange buttons in 2 columns
        return builder.as_markup()
