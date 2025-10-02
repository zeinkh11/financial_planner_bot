from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database import Base

class Message(Base):
    """Message model for storing conversation message pairs (user message + bot reply)."""
    
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    
    # User message fields
    user_telegram_message_id = Column(Integer, nullable=True)  # User's Telegram message ID
    user_content = Column(Text, nullable=False)  # User's message content
    user_sent_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Bot reply fields
    bot_telegram_message_id = Column(Integer, nullable=True)  # Bot's Telegram message ID
    bot_content = Column(Text, nullable=True)  # Bot's reply content
    bot_sent_at = Column(DateTime(timezone=True), nullable=True)
    
    # Status and metadata
    is_processed = Column(Boolean, default=False)  # Whether bot has processed and replied
    processing_time_ms = Column(Integer, nullable=True)  # Time taken to process in milliseconds
    
    
    # Relationships
    session = relationship("Session", back_populates="messages")
