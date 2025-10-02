# Contributing to Financial Planner Bot

Thank you for your interest in contributing to the Financial Planner Bot! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

Before creating an issue, please:
1. Check if the issue already exists
2. Use the issue templates provided
3. Include relevant information:
   - Python version
   - Operating system
   - Steps to reproduce
   - Expected vs actual behavior
   - Log files (if applicable)

### Suggesting Enhancements

We welcome feature requests! Please:
1. Check existing feature requests
2. Provide a clear description of the feature
3. Explain the use case and benefits
4. Consider implementation complexity

### Code Contributions

#### Setting Up Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/financial_planner_bot.git
   cd financial_planner_bot
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your development configuration:
   ```bash
   cp config.env.example config.env
   # Edit config.env with your test bot token and database settings
   ```

#### Development Guidelines

##### Code Style
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write clear, descriptive variable and function names
- Add docstrings to all functions and classes

##### Commit Messages
Use clear, descriptive commit messages:
```
feat: add budget tracking functionality
fix: resolve session timeout notification issue
docs: update README with installation instructions
refactor: improve database connection handling
```

##### Testing
- Test your changes thoroughly
- Ensure the bot starts without errors
- Test database operations
- Verify logging functionality

##### Pull Request Process

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots (if applicable)
   - Testing instructions

## 📋 Development Standards

### Architecture
- Follow the existing modular architecture
- Keep components loosely coupled
- Use dependency injection where appropriate
- Maintain separation of concerns

### Database
- Use async/await for all database operations
- Follow the existing service pattern
- Add proper error handling
- Include logging for database operations

### Logging
- Use appropriate log levels
- Include relevant context in log messages
- Use the centralized logging system
- Avoid logging sensitive information

### Error Handling
- Use specific exception types
- Provide meaningful error messages
- Log errors appropriately
- Handle edge cases gracefully

## 🏗️ Project Structure

Understanding the project structure helps with contributions:

```
├── bot.py                 # Main entry point
├── commands/              # Command handlers
├── core/                  # Core functionality
│   ├── config.py         # Configuration management
│   ├── logging_config.py # Logging system
│   └── session_timeout.py # Session management
└── database/              # Database layer
    ├── models/            # Database models
    └── services/          # Database services
```

## 🧪 Testing

### Manual Testing
1. Test bot startup and shutdown
2. Verify all commands work correctly
3. Test database operations
4. Check logging functionality
5. Test session timeout behavior

### Test Environment
- Use a test bot token (create via @BotFather)
- Use a separate test database
- Enable debug logging for detailed output

## 📚 Documentation

### Code Documentation
- Add docstrings to all functions and classes
- Include type hints
- Document complex algorithms
- Explain business logic

### User Documentation
- Update README.md for new features
- Add usage examples
- Document configuration options
- Provide troubleshooting guides

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment Information**:
   - Python version
   - Operating system
   - Bot version/commit

2. **Steps to Reproduce**:
   - Clear, numbered steps
   - Expected behavior
   - Actual behavior

3. **Additional Context**:
   - Log files (remove sensitive information)
   - Screenshots (if applicable)
   - Related issues

## 💡 Feature Requests

For feature requests, please provide:

1. **Problem Description**:
   - What problem does this solve?
   - Who would benefit from this feature?

2. **Proposed Solution**:
   - How should this work?
   - Any specific requirements?

3. **Alternatives Considered**:
   - What other solutions were considered?
   - Why is this approach preferred?

## 🔒 Security

### Reporting Security Issues
- **DO NOT** create public issues for security vulnerabilities
- Email security issues to: security@yourdomain.com
- Include detailed information about the vulnerability
- Allow time for response before public disclosure

### Security Guidelines
- Never commit sensitive information (tokens, passwords, keys)
- Use environment variables for configuration
- Validate all user inputs
- Follow secure coding practices

## 📞 Getting Help

- **Discord**: Join our community server
- **Issues**: Use GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Email**: Contact maintainers directly for urgent issues

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to the Financial Planner Bot! 🚀
