# Financial Planner Bot

A comprehensive Telegram bot for financial planning and management, built with Python and aiogram framework.

## 🚀 Features

- **Session Management**: Automatic session timeout handling with user notifications
- **Database Integration**: MySQL database with async SQLAlchemy ORM
- **Comprehensive Logging**: Separate log files for different components (bot, database, session, app, error)
- **Modular Architecture**: Clean separation of concerns with organized command handlers
- **User Management**: Complete user registration and session tracking
- **Message History**: Persistent message storage for conversation context

## 📋 Prerequisites

- Python 3.8+
- MySQL 5.7+ or MySQL 8.0+
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/financial_planner_bot.git
cd financial_planner_bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

1. Create a MySQL database:
```sql
CREATE DATABASE financial_planner_bot CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Run the SQL script to create tables:
```bash
mysql -u root -p financial_planner_bot < create_tables.sql
```

### 5. Configuration

1. Copy the example configuration file:
```bash
cp config.env.example config.env
```

2. Edit `config.env` with your settings:
```env
# Bot Configuration
BOT_TOKEN=your_bot_token_here
BOT_NAME=Financial Planner Bot
BOT_DESCRIPTION=A simple financial planner bot

# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_NAME=financial_planner_bot
DB_USER=root
DB_PASSWORD=your_mysql_password

# Session Configuration
SESSION_TIME=30  # Session timeout in minutes

# Logging Configuration
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_DIR=logs
LOG_MAX_SIZE=10485760  # 10MB
LOG_BACKUP_COUNT=5

# Optional Settings
DEBUG=False
```

## 🚀 Running the Bot

```bash
python bot.py
```

The bot will:
- Initialize the logging system
- Connect to the database
- Start the session timeout checker
- Begin polling for Telegram messages

## 📁 Project Structure

```
financial_planner_bot/
├── bot.py                 # Main bot entry point
├── requirements.txt       # Python dependencies
├── create_tables.sql     # Database schema
├── config.env.example    # Configuration template
├── .gitignore            # Git ignore rules
├── README.md            # This file
├── commands/            # Command handlers
│   ├── __init__.py
│   ├── base.py          # Base command class
│   ├── start.py         # /start command
│   ├── menu.py          # Main menu
│   ├── help.py          # /help command
│   ├── echo.py          # Echo handler
│   ├── callbacks.py     # Callback handlers
│   └── handlers.py      # Handler registration
├── core/                # Core functionality
│   ├── __init__.py
│   ├── config.py        # Configuration management
│   ├── logging_config.py # Logging system
│   └── session_timeout.py # Session timeout handler
└── database/            # Database layer
    ├── __init__.py
    ├── database.py      # Database connection
    ├── models/          # Database models
    │   ├── __init__.py
    │   ├── user.py      # User model
    │   ├── session.py   # Session model
    │   └── message.py   # Message model
    └── services/        # Database services
        ├── __init__.py
        ├── user_service.py
        ├── session_service.py
        └── message_service.py
```

## 🔧 Configuration Options

### Bot Configuration
- `BOT_TOKEN`: Your Telegram bot token
- `BOT_NAME`: Bot display name
- `BOT_DESCRIPTION`: Bot description

### Database Configuration
- `DB_HOST`: MySQL host (default: localhost)
- `DB_PORT`: MySQL port (default: 3306)
- `DB_NAME`: Database name
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password
- `DB_CHARSET`: Character set (default: utf8mb4)

### Session Configuration
- `SESSION_TIME`: Session timeout in minutes (default: 30)

### Logging Configuration
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `LOG_DIR`: Log directory (default: logs)
- `LOG_MAX_SIZE`: Maximum log file size in bytes (default: 10MB)
- `LOG_BACKUP_COUNT`: Number of backup log files (default: 5)

### Optional Settings
- `DEBUG`: Enable debug mode (default: False)

## 📊 Logging System

The bot uses a comprehensive logging system with separate log files:

- **`logs/bot.log`**: Bot operations and Telegram interactions
- **`logs/database.log`**: Database operations and queries
- **`logs/session.log`**: Session management and timeouts
- **`logs/app.log`**: General application events
- **`logs/error.log`**: Error and critical messages

Log files are automatically rotated when they reach the maximum size.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/financial_planner_bot/issues) page
2. Create a new issue with detailed information
3. Check the log files in the `logs/` directory for error details

## 🔮 Roadmap

- [ ] Financial goal tracking
- [ ] Budget management
- [ ] Expense categorization
- [ ] Investment tracking
- [ ] Financial reports
- [ ] Multi-language support
- [ ] Web dashboard
- [ ] API endpoints

## 🙏 Acknowledgments

- [aiogram](https://github.com/aiogram/aiogram) - Modern Telegram Bot API framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and ORM
- [asyncio](https://docs.python.org/3/library/asyncio.html) - Asynchronous I/O framework

## 📞 Contact

Your Name - [@yourusername](https://github.com/yourusername)

Project Link: [https://github.com/yourusername/financial_planner_bot](https://github.com/yourusername/financial_planner_bot)