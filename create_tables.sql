
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_id INT UNIQUE NOT NULL,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_telegram_id (telegram_id)
);


CREATE TABLE sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    context_data TEXT,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP NULL,
    last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_is_active (is_active),
    INDEX idx_last_activity (last_activity)
);


CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    user_telegram_message_id INT,
    user_content TEXT NOT NULL,
    user_sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    bot_telegram_message_id INT,
    bot_content TEXT,
    bot_sent_at TIMESTAMP NULL,
    is_processed BOOLEAN DEFAULT FALSE,
    processing_time_ms INT,
    
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
    INDEX idx_session_id (session_id),
    INDEX idx_user_telegram_message_id (user_telegram_message_id),
    INDEX idx_bot_telegram_message_id (bot_telegram_message_id),
    INDEX idx_is_processed (is_processed),
    INDEX idx_user_sent_at (user_sent_at)
);