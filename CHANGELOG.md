# Changelog

All notable changes to the Financial Planner Bot project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive logging system with separate log files
- Session timeout management with user notifications
- Database models for users, sessions, and messages
- Modular command handler architecture
- Configuration management system
- GitHub Actions CI/CD pipeline
- Comprehensive documentation

### Changed
- Replaced all print statements with proper logging
- Improved error handling throughout the application
- Enhanced database connection management

### Fixed
- Session timeout notification issues
- Database connection stability
- Logging configuration problems

## [1.0.0] - 2024-01-XX

### Added
- Initial release of Financial Planner Bot
- Basic bot functionality with aiogram framework
- MySQL database integration with SQLAlchemy
- User registration and session management
- Message history tracking
- Session timeout handling
- Comprehensive logging system
- Modular architecture with separate components

### Features
- **Bot Commands**: Start, help, menu, echo commands
- **Session Management**: Automatic session timeout with notifications
- **Database Integration**: Async MySQL operations with proper error handling
- **Logging System**: Separate log files for different components
- **Configuration**: Environment-based configuration management
- **Error Handling**: Comprehensive error handling and logging

### Technical Details
- Python 3.8+ support
- Async/await pattern throughout
- SQLAlchemy ORM with async support
- Rotating log files with configurable size limits
- Environment-based configuration
- Modular command handler system

## [0.1.0] - 2024-01-XX

### Added
- Project initialization
- Basic bot structure
- Database models
- Command handlers
- Session management
- Logging configuration

---

## Version Numbering

This project uses [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

## Release Process

1. Update version numbers in `setup.py`
2. Update this changelog
3. Create a git tag for the version
4. Push changes and tags to GitHub
5. GitHub Actions will automatically create a release

## Contributing

When contributing to this project, please:

1. Add your changes to the "Unreleased" section
2. Use the following format:
   - **Added** for new features
   - **Changed** for changes in existing functionality
   - **Deprecated** for soon-to-be removed features
   - **Removed** for now removed features
   - **Fixed** for any bug fixes
   - **Security** for vulnerability fixes

3. Follow the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format
