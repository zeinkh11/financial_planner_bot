#!/usr/bin/env python3
"""
Setup script for Financial Planner Bot
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="financial-planner-bot",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive Telegram bot for financial planning and management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/financial_planner_bot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Communications :: Chat",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.18.0",
            "pytest-cov>=2.12.0",
            "flake8>=3.9.0",
            "black>=21.0.0",
            "isort>=5.9.0",
            "mypy>=0.910",
            "bandit>=1.7.0",
            "safety>=1.10.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "financial-planner-bot=bot:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.sql", "*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords="telegram bot financial planning aiogram async python",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/financial_planner_bot/issues",
        "Source": "https://github.com/yourusername/financial_planner_bot",
        "Documentation": "https://github.com/yourusername/financial_planner_bot#readme",
    },
)
