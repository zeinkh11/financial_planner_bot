"""
Database package for Financial Planner Bot.
Contains database connection, models, and services.
"""

from .database import (
    Base,
    db_manager,
    get_db_session,
    init_database,
    close_database,
    test_database_connection
)

from .models import (
    User,
    Session,
    Message
)

from .services import (
    UserService,
    SessionService,
    MessageService
)

__all__ = [
    # Database connection
    'Base',
    'db_manager',
    'get_db_session',
    'init_database',
    'close_database',
    'test_database_connection',
    
    # Models
    'User',
    'Session',
    'Message',
    
    # Services
    'UserService',
    'SessionService',
    'MessageService'
]
